from src.intake_service import filter_handoff_rows


def _rows():
    return [
        {"owner": "platform", "severity": "low", "summary": "Copy cleanup"},
        {"owner": "support", "severity": "high", "summary": "Queue delay"},
        {"owner": "release", "severity": "critical", "summary": "Train blocked"},
        {"owner": "qa", "severity": "medium", "summary": "Flaky test"},
    ]


def test_default_is_pass_through_in_order():
    rows = _rows()
    assert filter_handoff_rows(rows) == rows


def test_min_severity_high_keeps_high_and_critical():
    kept = filter_handoff_rows(_rows(), min_severity="high")
    assert [row["severity"] for row in kept] == ["high", "critical"]


def test_min_severity_medium_preserves_input_order():
    kept = filter_handoff_rows(_rows(), min_severity="medium")
    assert [row["owner"] for row in kept] == ["support", "release", "qa"]


def test_unknown_severity_ranks_lowest_and_is_dropped():
    rows = [{"owner": "x", "severity": "bogus", "summary": "s"}]
    assert filter_handoff_rows(rows, min_severity="low") == []


def test_unknown_min_severity_is_rejected():
    rows = [{"owner": "platform", "severity": "high", "summary": "Queue delay"}]

    try:
        filter_handoff_rows(rows, min_severity="urgent")
    except ValueError as exc:
        assert "unknown minimum severity: urgent" in str(exc)
    else:
        raise AssertionError("unknown min_severity should be rejected")