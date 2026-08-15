from __future__ import annotations

import sqlite3
import tempfile
import unittest
from pathlib import Path

from agent_harness import (
    Harness,
    Message,
    ModelTurn,
    RecentContextBuilder,
    ScriptedProvider,
    SQLiteSessionStore,
    StopReason,
)


class ContextTests(unittest.TestCase):
    def test_recent_builder_preserves_system_and_newest_messages(self):
        builder = RecentContextBuilder(max_characters=8)

        bundle = builder.build(
            [Message("system", "sys"), Message("user", "old!"), Message("user", "new!!")]
        )

        self.assertEqual(["sys", "new!!"], [m.content for m in bundle.messages])
        self.assertEqual(1, bundle.dropped_messages)
        self.assertEqual(8, bundle.used_characters)

    def test_context_failure_is_an_explicit_stop_reason(self):
        provider = ScriptedProvider([ModelTurn(content="not reached")])
        harness = Harness(provider, context_builder=RecentContextBuilder(5))

        result = harness.run("context-fail", "hello")

        self.assertEqual(StopReason.CONTEXT_ERROR, result.stop_reason)
        self.assertEqual(0, len(provider.requests))
        event_kinds = [event.kind for event in result.events]
        self.assertIn("context.failed", event_kinds)
        self.assertNotIn("model.requested", event_kinds)

    def test_recent_builder_keeps_a_contiguous_recent_suffix(self):
        builder = RecentContextBuilder(max_characters=8)

        bundle = builder.build(
            [
                Message("system", "s"),
                Message("user", "old"),
                Message("user", "too-big"),
                Message("user", "new"),
            ]
        )

        self.assertEqual(["s", "new"], [message.content for message in bundle.messages])
        self.assertEqual(2, bundle.dropped_messages)


class SQLiteStoreTests(unittest.TestCase):
    def test_session_messages_and_events_survive_store_reopen(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sessions.sqlite3"
            with SQLiteSessionStore(path) as first_store:
                first = Harness(
                    ScriptedProvider([ModelTurn(content="first")]), store=first_store
                )
                first_result = first.run("persistent", "one")
                first_event_count = len(first_result.events)

            with SQLiteSessionStore(path) as second_store:
                provider = ScriptedProvider([ModelTurn(content="second")])
                second = Harness(provider, store=second_store)
                second_result = second.run("persistent", "two")
                checkpoint = second_store.checkpoint("persistent")

            visible_contents = [message.content for message in provider.requests[0][0]]
            self.assertIn("first", visible_contents)
            self.assertEqual(first_event_count, len(second_result.events))
            self.assertNotEqual(first_result.attempt_id, second_result.attempt_id)
            self.assertTrue(
                all(
                    event.attempt_id == second_result.attempt_id
                    for event in second_result.events
                )
            )
            self.assertGreater(len(checkpoint["events"]), first_event_count)
            self.assertEqual("run.finished", checkpoint["events"][-1]["kind"])
            self.assertEqual("second", checkpoint["messages"][-1]["content"])

    def test_legacy_event_schema_is_migrated_without_losing_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "legacy.sqlite3"
            connection = sqlite3.connect(path)
            connection.execute(
                """
                CREATE TABLE events (
                    session_id TEXT NOT NULL,
                    sequence INTEGER NOT NULL,
                    kind TEXT NOT NULL,
                    data_json TEXT NOT NULL,
                    PRIMARY KEY (session_id, sequence)
                )
                """
            )
            connection.execute(
                "INSERT INTO events VALUES (?, ?, ?, ?)",
                ("legacy-session", 1, "legacy.event", "{}"),
            )
            connection.commit()
            connection.close()

            with SQLiteSessionStore(path) as store:
                events = store.events("legacy-session")

            self.assertEqual(1, len(events))
            self.assertEqual("legacy", events[0].attempt_id)


if __name__ == "__main__":
    unittest.main()
