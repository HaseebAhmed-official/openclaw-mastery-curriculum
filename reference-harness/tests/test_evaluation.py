from __future__ import annotations

import unittest

from agent_harness import EvalTask, Harness, ModelTurn, ScriptedProvider, run_eval


class EvaluationTests(unittest.TestCase):
    def test_repeated_trials_report_pass_rate_and_keep_runs(self):
        task = EvalTask(
            task_id="final-answer",
            prompt="answer",
            grader=lambda run: (run.output == "ok", "output must equal ok"),
        )

        report = run_eval(
            [task],
            lambda trial: Harness(
                ScriptedProvider([ModelTurn(content="ok" if trial < 3 else "bad")])
            ),
            trials_per_task=3,
        )

        self.assertAlmostEqual(2 / 3, report.pass_rate)
        self.assertEqual(3, len(report.trials))
        self.assertEqual("final-answer-3", report.trials[2].run.session_id)

    def test_zero_trials_is_rejected(self):
        with self.assertRaises(ValueError):
            run_eval([], lambda _: Harness(ScriptedProvider([])), trials_per_task=0)


if __name__ == "__main__":
    unittest.main()
