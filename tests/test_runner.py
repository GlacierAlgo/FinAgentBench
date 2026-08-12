from finagentbench.runner import render_markdown_report, summarize_results


def _result(model: str, score: float, latency: float) -> dict:
    return {
        "model": model,
        "case_id": "case-a",
        "status": "completed",
        "latency_seconds": latency,
        "score": {
            "total": score,
            "prediction_correct": True,
            "premise_correct": True,
            "evidence_f1": 1.0,
        },
        "usage": {
            "input_tokens": 100,
            "cached_input_tokens": 20,
            "output_tokens": 10,
        },
    }


def test_summary_aggregates_by_model() -> None:
    summary = summarize_results([_result("model-a", 80, 2), _result("model-a", 100, 4)])

    assert summary == [
        {
            "model": "model-a",
            "completed": 2,
            "failed": 0,
            "mean_score": 90.0,
            "prediction_accuracy": 1.0,
            "premise_accuracy": 1.0,
            "mean_evidence_f1": 1.0,
            "mean_latency_seconds": 3.0,
            "input_tokens": 200,
            "cached_input_tokens": 40,
            "output_tokens": 20,
        }
    ]


def test_report_discloses_ceiling_effect() -> None:
    results = [_result("model-a", 100, 2)]
    run = {
        "harness": {"version": "codex-cli test"},
        "matrix": {
            "reasoning_effort": "low",
            "case_count": 1,
            "repeats": 1,
            "case_suite_sha256": "abc123",
        },
        "summary": summarize_results(results),
        "results": results,
    }

    report = render_markdown_report(run)

    assert "Case suite: `abc123`" in report
    assert "ceiling effect" in report
