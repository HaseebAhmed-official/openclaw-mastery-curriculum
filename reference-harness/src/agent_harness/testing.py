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


@dataclass(frozen=True)
class EvalTask:
    task_id: str
    prompt: str
    grader: Grader
    critical: bool = False


HarnessFactory = Callable[[EvalTask, int], Harness]


@dataclass(frozen=True)
class EvalPolicy:
    trials_per_task: int = 3
    min_overall_pass_rate: float = 0.8
    min_task_pass_rate: float = 0.5
    fail_on_critical_trial: bool = True

    def __post_init__(self) -> None:
        if self.trials_per_task < 1:
            raise ValueError("trials_per_task must be positive")
        for name, value in (
            ("min_overall_pass_rate", self.min_overall_pass_rate),
            ("min_task_pass_rate", self.min_task_pass_rate),
        ):
            if not 0 <= value <= 1:
                raise ValueError(f"{name} must be between zero and one")


@dataclass(frozen=True)
class TrialResult:
    task_id: str
    trial: int
    passed: bool
    reason: str
    run: RunResult | None
    critical: bool = False


@dataclass(frozen=True)
class EvalDecision:
    approved: bool
    reasons: tuple[str, ...]


@dataclass(frozen=True)
class EvalReport:
    trials: tuple[TrialResult, ...]
    policy: EvalPolicy

    @property
    def pass_rate(self) -> float:
        if not self.trials:
            return 0.0
        return sum(trial.passed for trial in self.trials) / len(self.trials)

    @property
    def task_pass_rates(self) -> dict[str, float]:
        task_ids = sorted({trial.task_id for trial in self.trials})
        return {
            task_id: sum(
                trial.passed for trial in self.trials if trial.task_id == task_id
            )
            / sum(1 for trial in self.trials if trial.task_id == task_id)
            for task_id in task_ids
        }

    @property
    def decision(self) -> EvalDecision:
        reasons: list[str] = []
        if not self.trials:
            reasons.append("no evaluation trials were executed")
        if self.pass_rate < self.policy.min_overall_pass_rate:
            reasons.append("overall pass rate is below the predeclared threshold")
        below_task_threshold = [
            task_id
            for task_id, rate in self.task_pass_rates.items()
            if rate < self.policy.min_task_pass_rate
        ]
        if below_task_threshold:
            reasons.append(
                "task pass rate is below threshold: "
                + ", ".join(below_task_threshold)
            )
        if self.policy.fail_on_critical_trial and any(
            trial.critical and not trial.passed for trial in self.trials
        ):
            reasons.append("at least one critical trial failed")
        return EvalDecision(approved=not reasons, reasons=tuple(reasons))


def run_eval(
    tasks: Iterable[EvalTask],
    harness_factory: HarnessFactory,
    trials_per_task: int | None = None,
    *,
    policy: EvalPolicy | None = None,
) -> EvalReport:
    if policy is None:
        policy = EvalPolicy(
            trials_per_task=3 if trials_per_task is None else trials_per_task
        )
    elif trials_per_task is not None and trials_per_task != policy.trials_per_task:
        raise ValueError("trials_per_task conflicts with the evaluation policy")

    task_list = tuple(tasks)
    task_ids = [task.task_id for task in task_list]
    if any(not task_id for task_id in task_ids):
        raise ValueError("task ids must be non-empty")
    if len(set(task_ids)) != len(task_ids):
        raise ValueError("task ids must be unique")

    results: list[TrialResult] = []
    for task in task_list:
        for trial in range(1, policy.trials_per_task + 1):
            run: RunResult | None = None
            try:
                harness = harness_factory(task, trial)
                run = harness.run(f"{task.task_id}-{trial}", task.prompt)
                passed, reason = task.grader(run)
                if not isinstance(passed, bool) or not isinstance(reason, str):
                    raise TypeError("grader must return (bool, str)")
            except Exception as exc:
                passed = False
                reason = f"evaluation infrastructure error: {type(exc).__name__}: {exc}"
            results.append(
                TrialResult(task.task_id, trial, passed, reason, run, task.critical)
            )
    return EvalReport(tuple(results), policy)
