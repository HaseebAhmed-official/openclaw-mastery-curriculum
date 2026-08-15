"""Single-process SQLite teaching store for messages, events, and reset recovery."""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from .contracts import Event, JsonObject, Message


class SQLiteSessionStore:
    """Persist session evidence without claiming distributed workflow semantics."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self._connection = sqlite3.connect(self.path)
        self._connection.execute("PRAGMA foreign_keys = ON")
        self._connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS messages (
                session_id TEXT NOT NULL,
                sequence INTEGER NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                name TEXT,
                call_id TEXT,
                metadata_json TEXT NOT NULL,
                PRIMARY KEY (session_id, sequence)
            );
            CREATE TABLE IF NOT EXISTS events (
                session_id TEXT NOT NULL,
                sequence INTEGER NOT NULL,
                attempt_id TEXT NOT NULL,
                kind TEXT NOT NULL,
                data_json TEXT NOT NULL,
                PRIMARY KEY (session_id, sequence)
            );
            """
        )
        event_columns = {
            row[1] for row in self._connection.execute("PRAGMA table_info(events)")
        }
        if "attempt_id" not in event_columns:
            self._connection.execute(
                "ALTER TABLE events ADD COLUMN attempt_id TEXT NOT NULL DEFAULT 'legacy'"
            )
        self._connection.commit()

    def close(self) -> None:
        self._connection.close()

    def __enter__(self) -> "SQLiteSessionStore":
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def messages(self, session_id: str) -> tuple[Message, ...]:
        rows = self._connection.execute(
            """
            SELECT role, content, name, call_id, metadata_json
            FROM messages WHERE session_id = ? ORDER BY sequence
            """,
            (session_id,),
        ).fetchall()
        return tuple(
            Message(role, content, name, call_id, json.loads(metadata_json))
            for role, content, name, call_id, metadata_json in rows
        )

    def events(self, session_id: str) -> tuple[Event, ...]:
        rows = self._connection.execute(
            """
            SELECT sequence, attempt_id, kind, data_json
            FROM events WHERE session_id = ? ORDER BY sequence
            """,
            (session_id,),
        ).fetchall()
        return tuple(
            Event(sequence, session_id, attempt_id, kind, json.loads(data_json))
            for sequence, attempt_id, kind, data_json in rows
        )

    def append_message(self, session_id: str, message: Message) -> None:
        with self._connection:
            sequence = self._next_sequence("messages", session_id)
            self._connection.execute(
                """
                INSERT INTO messages
                    (session_id, sequence, role, content, name, call_id, metadata_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    session_id,
                    sequence,
                    message.role,
                    message.content,
                    message.name,
                    message.call_id,
                    json.dumps(dict(message.metadata), sort_keys=True, default=str),
                ),
            )

    def append_event(
        self, session_id: str, attempt_id: str, kind: str, data: JsonObject
    ) -> Event:
        with self._connection:
            sequence = self._next_sequence("events", session_id)
            event = Event(sequence, session_id, attempt_id, kind, dict(data))
            self._connection.execute(
                """
                INSERT INTO events
                    (session_id, sequence, attempt_id, kind, data_json)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    session_id,
                    sequence,
                    attempt_id,
                    kind,
                    json.dumps(dict(data), sort_keys=True, default=str),
                ),
            )
        return event

    def checkpoint(self, session_id: str) -> JsonObject:
        return {
            "messages": [
                {
                    "role": message.role,
                    "content": message.content,
                    "name": message.name,
                    "call_id": message.call_id,
                    "metadata": dict(message.metadata),
                }
                for message in self.messages(session_id)
            ],
            "events": [
                {
                    "sequence": event.sequence,
                    "session_id": event.session_id,
                    "attempt_id": event.attempt_id,
                    "kind": event.kind,
                    "data": dict(event.data),
                }
                for event in self.events(session_id)
            ],
        }

    def _next_sequence(self, table: str, session_id: str) -> int:
        if table not in {"messages", "events"}:
            raise ValueError("unsupported sequence table")
        row = self._connection.execute(
            f"SELECT COALESCE(MAX(sequence), 0) + 1 FROM {table} WHERE session_id = ?",
            (session_id,),
        ).fetchone()
        return int(row[0])
