from src.ai_explainer import explain_reason

def test_ai_explanation_runs():
    result = explain_reason("genre match (+1.0), energy similarity (+0.9)")
    assert isinstance(result, str)
    assert len(result) > 0