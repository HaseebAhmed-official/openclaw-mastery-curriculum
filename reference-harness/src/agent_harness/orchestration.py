"""Deterministic orchestration fixtures with explicit budgets and failures."""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass

Worker = Callable[[str], str]


@dataclass(frozen=True)
class WorkerResult:
    worker: str
    ok: bool
    output: str = ""
    error: str = ""


@dataclass(frozen=True)
class OrchestrationReport:
    pattern: str
    results: tuple[WorkerResult, ...]

    @property
    def failed_workers(self) -> tuple[str, ...]:
        return tuple(result.worker for result in self.results if not result.ok)


def run_routed(
    task: str, route: str, workers: Mapping[str, Worker]
) -> OrchestrationReport:
    if route not in workers:
        raise ValueError(f"unknown route: {route}")
    return OrchestrationReport("route", (_invoke(route, workers[route], task),))


def run_fan_out_sequential(
    task: str,
    worker_names: Sequence[str],
    workers: Mapping[str, Worker],
    *,
    max_workers: int,
) -> OrchestrationReport:
    """Run a deterministic fan-out fixture; this is intentionally not concurrent."""

    if max_workers < 1:
        raise ValueError("max_workers must be positive")
    if not worker_names:
        raise ValueError("fan-out requires at least one worker")
    if len(worker_names) > max_workers:
        raise ValueError("fan-out exceeds the declared worker budget")
    if len(set(worker_names)) != len(worker_names):
        raise ValueError("duplicate workers would repeat work")
    unknown = [name for name in worker_names if name not in workers]
    if unknown:
        raise ValueError(f"unknown workers: {', '.join(sorted(unknown))}")

    results = tuple(_invoke(name, workers[name], task) for name in worker_names)
    return OrchestrationReport("fan_out_sequential", results)


def _invoke(name: str, worker: Worker, task: str) -> WorkerResult:
    try:
        output = worker(task)
        if not isinstance(output, str):
            raise TypeError("worker must return a string")
        return WorkerResult(worker=name, ok=True, output=output)
    except Exception as exc:  # noqa: BLE001 - worker failures become evidence.
        return WorkerResult(worker=name, ok=False, error=f"{type(exc).__name__}: {exc}")
