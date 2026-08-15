"""Bounded memory fixture with provenance, isolation, expiry, and deletion."""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass, field

from .contracts import JsonObject

MemoryWritePolicy = Callable[["MemoryRecord"], tuple[bool, str]]


@dataclass(frozen=True)
class MemoryRecord:
    memory_id: str
    namespace: str
    content: str
    source: str
    created_at: float
    expires_at: float | None = None
    metadata: JsonObject = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not all((self.memory_id, self.namespace, self.content, self.source)):
            raise ValueError("memory identity, namespace, content, and source are required")
        if self.expires_at is not None and self.expires_at <= self.created_at:
            raise ValueError("memory expiry must be later than creation")


@dataclass(frozen=True)
class MemoryHit:
    record: MemoryRecord
    score: float
    trust: str = "untrusted"


class InMemoryMemoryStore:
    """A deterministic teaching store, not a vector database or durable service."""

    def __init__(self, write_policy: MemoryWritePolicy) -> None:
        self._write_policy = write_policy
        self._records: dict[str, MemoryRecord] = {}

    def put(self, record: MemoryRecord) -> None:
        decision = self._write_policy(record)
        if (
            not isinstance(decision, tuple)
            or len(decision) != 2
            or not isinstance(decision[0], bool)
            or not isinstance(decision[1], str)
        ):
            raise TypeError("memory write policy must return (bool, str)")
        allowed, reason = decision
        if not allowed:
            raise PermissionError(reason)
        if record.memory_id in self._records:
            raise ValueError(f"duplicate memory id: {record.memory_id}")
        self._records[record.memory_id] = record

    def search(
        self, namespace: str, query: str, *, now: float, limit: int = 5
    ) -> tuple[MemoryHit, ...]:
        if not namespace:
            raise ValueError("namespace is required")
        if limit < 1:
            raise ValueError("limit must be positive")
        query_tokens = _tokens(query)
        if not query_tokens:
            return ()

        hits: list[MemoryHit] = []
        for record in self._records.values():
            if record.namespace != namespace:
                continue
            if record.expires_at is not None and record.expires_at <= now:
                continue
            record_tokens = _tokens(record.content)
            overlap = query_tokens & record_tokens
            if not overlap:
                continue
            score = len(overlap) / len(query_tokens)
            hits.append(MemoryHit(record=record, score=score))

        hits.sort(
            key=lambda hit: (-hit.score, -hit.record.created_at, hit.record.memory_id)
        )
        return tuple(hits[:limit])

    def delete(self, namespace: str, memory_id: str) -> bool:
        record = self._records.get(memory_id)
        if record is None or record.namespace != namespace:
            return False
        del self._records[memory_id]
        return True

    def records(self, namespace: str) -> tuple[MemoryRecord, ...]:
        return tuple(
            sorted(
                (
                    record
                    for record in self._records.values()
                    if record.namespace == namespace
                ),
                key=lambda record: (record.created_at, record.memory_id),
            )
        )


def _tokens(value: str) -> frozenset[str]:
    return frozenset(re.findall(r"[a-z0-9]+", value.casefold()))
