"""Deterministic context selection with explicit budget evidence."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .contracts import ContextBundle, Message


class ContextBudgetError(ValueError):
    """Raised when required context cannot fit without silent truncation."""


@dataclass(frozen=True)
class AllContextBuilder:
    def build(self, messages: Sequence[Message]) -> ContextBundle:
        selected = tuple(messages)
        return ContextBundle(
            messages=selected,
            used_characters=sum(len(message.content) for message in selected),
            dropped_messages=0,
        )


@dataclass(frozen=True)
class RecentContextBuilder:
    max_characters: int

    def __post_init__(self) -> None:
        if self.max_characters < 1:
            raise ValueError("max_characters must be positive")

    def build(self, messages: Sequence[Message]) -> ContextBundle:
        systems = [message for message in messages if message.role == "system"]
        conversation = [message for message in messages if message.role != "system"]
        system_size = sum(len(message.content) for message in systems)
        if system_size > self.max_characters:
            raise ContextBudgetError("trusted system instructions exceed context budget")

        remaining = self.max_characters - system_size
        selected_reversed: list[Message] = []
        dropped = 0
        for message in reversed(conversation):
            size = len(message.content)
            if size <= remaining:
                selected_reversed.append(message)
                remaining -= size
            else:
                dropped = len(conversation) - len(selected_reversed)
                break

        if conversation and not selected_reversed:
            raise ContextBudgetError("latest conversation message exceeds context budget")

        selected = tuple(systems + list(reversed(selected_reversed)))
        return ContextBundle(
            messages=selected,
            used_characters=self.max_characters - remaining,
            dropped_messages=dropped,
        )
