from __future__ import annotations

import unittest
from typing import cast

from agent_harness import (
    EvalPolicy,
    EvalTask,
    Harness,
    ModelTurn,
    ScriptedProvider,
    run_eval,
)
from agent_harness.testing import Grader


class EvaluationTests(unittest.TestCase):
    def test_repeated_trials_report_pass_rate_and_keep_runs(self):
        task = EvalTask(
            task_id="final-answer",
            prompt="answer",
            grader=lambda run: (run.output == "ok", "output must equal ok"),
        )

        report = run_eval(
            [task],
            lambda _task, trial: Harness(
                ScriptedProvider([ModelTurn(content="ok" if trial < 3 else "bad")])
            ),
            policy=EvalPolicy(
                trials_per_task=3,
                min_overall_pass_rate=2 / 3,
                min_task_pass_rate=2 / 3,
            ),
        )

        self.assertAlmostEqual(2 / 3, report.pass_rate)
        self.assertEqual(3, len(report.trials))
        final_run = report.trials[2].run
        assert final_run is not None
        self.assertEqual("final-answer-3", final_run.session_id)
        self.assertTrue(report.decision.approved)

    def test_critical_failure_rejects_release_even_when_average_passes(self):
        tasks = [
            EvalTask("ordinary", "answer", lambda run: (True, "pass")),
            EvalTask(
                "security",
                "deny",
                lambda run: (run.output == "deny", "must deny"),
                critical=True,
            ),
        ]
        policy = EvalPolicy(
            trials_per_task=2,
            min_overall_pass_rate=0.5,
            min_task_pass_rate=0.0,
            fail_on_critical_trial=True,
        )

        report = run_eval(
            tasks,
            lambda task, _trial: Harness(
                ScriptedProvider(
                    [ModelTurn(content="allow" if task.task_id == "security" else "ok")]
                )
            ),
            policy=policy,
        )

        self.assertFalse(report.decision.approved)
        self.assertIn("at least one critical trial failed", report.decision.reasons)
        self.assertEqual(0.0, report.task_pass_rates["security"])

    def test_zero_trials_is_rejected(self):
        with self.assertRaises(ValueError):
            run_eval(
                [],
                lambda _task, _trial: Harness(ScriptedProvider([])),
                trials_per_task=0,
            )

    def test_infrastructure_failure_vetoes_even_permissive_thresholds(self):
        def broken_factory(_task, _trial):
            raise RuntimeError("synthetic factory failure")

        def broken_grader(_run):
            raise ValueError("synthetic grader failure")

        policy = EvalPolicy(
            trials_per_task=1,
            min_overall_pass_rate=0,
            min_task_pass_rate=0,
            fail_on_critical_trial=False,
        )
        for failure in ("factory", "grader", "invalid_grade"):
            with self.subTest(failure=failure):
                grader = (
                    broken_grader
                    if failure == "grader"
                    else (lambda run: ("yes", "invalid boolean"))
                    if failure == "invalid_grade"
                    else (lambda run: (True, "ok"))
                )
                report = run_eval(
                    # Deliberately cross the typed boundary to test runtime rejection.
                    [EvalTask("infrastructure", "answer", cast(Grader, grader))],
                    broken_factory
                    if failure == "factory"
                    else (
                        lambda task, trial: Harness(
                            ScriptedProvider([ModelTurn(content="ok")])
                        )
                    ),
                    policy=policy,
                )
                self.assertFalse(report.decision.approved)
                self.assertTrue(report.trials[0].infrastructure_error)
                self.assertIn(
                    "evaluation infrastructure failed; release evidence is incomplete",
                    report.decision.reasons,
                )
                self.assertEqual(failure == "factory", report.trials[0].run is None)

    def test_valid_negative_grade_remains_a_task_failure_not_infrastructure(self):
        report = run_eval(
            [
                EvalTask(
                    "ordinary-failure",
                    "answer",
                    lambda run: (False, "incorrect answer"),
                )
            ],
            lambda task, trial: Harness(ScriptedProvider([ModelTurn(content="wrong")])),
            policy=EvalPolicy(
                trials_per_task=1, min_overall_pass_rate=0, min_task_pass_rate=0
            ),
        )
        self.assertFalse(report.trials[0].infrastructure_error)
        self.assertFalse(report.trials[0].passed)
        self.assertTrue(report.decision.approved)


if __name__ == "__main__":
    unittest.main()
