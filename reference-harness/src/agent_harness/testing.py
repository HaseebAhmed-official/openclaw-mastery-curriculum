"""Deterministic provider and repeated-trial evaluation helpers."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable, Iterable, Sequence

from .contracts import JsonObject, Message, ModelTurn, Provider, RunResult
from .runtime import Harness


class ScriptedProvider(Provider):
    def __init__(self, turns: Iterable[ModelTurn]) -> None:
        self._turns = deque(turns)
        self.requests: list[tuple[tuple[Message, ...], tuple[JsonObject, ...]]] = []

    def complete(
        self, messages: Sequence[Message], tools: Sequence[JsonObject]
    ) -> ModelTurn:
        self.requests.append((tuple(messages), tuple(tools)))
        if not self._turns:
            raise RuntimeError("scripted provider has no remaining turns")
        return self._turns.popleft()


Grader = Callable[[RunResult], tuple[bool, str]]
HarnessFactory = Callable[[int], Harness]


@dataclass(frozen=True)
class EvalTask:
    task_id: str
    prompt: str
    grader: Grader


@dataclass(frozen=True)
class TrialResult:
    task_id: str
    trial: int
    passed: bool
    reason: str
    run: RunResult


@dataclass(frozen=True)
class EvalReport:
    trials: tuple[TrialResult, ...]

    @property
    def pass_rate(self) -> float:
        if not self.trials:
            return 0.0
        return sum(trial.passed for trial in self.trials) / len(self.trials)


def run_eval(
    tasks: Iterable[EvalTask],
    harness_factory: HarnessFactory,
    trials_per_task: int = 3,
) -> EvalReport:
    if trials_per_task < 1:
        raise ValueError("trials_per_task must be positive")

    results: list[TrialResult] = []
    for task in tasks:
        for trial in range(1, trials_per_task + 1):
            harness = harness_factory(trial)
            run = harness.run(f"{task.task_id}-{trial}", task.prompt)
            passed, reason = task.grader(run)
            results.append(
                TrialResult(task.task_id, trial, passed, reason, run)
            )
    return EvalReport(tuple(results))
