from datetime import datetime, timezone

from src.tc1_service import OperationSignal, summarize_signals_for_handoff


def _ts():
    return datetime(2026, 5, 30, tzinfo=timezone.utc)


def _signals():
    return [
        OperationSignal("docs-drift", "low", "docs", _ts()),
        OperationSignal("queue-delay", "high", "platform", _ts()),
        OperationSignal("release-blocker", "critical", "release", _ts()),
        OperationSignal("flake", "medium", "qa", _ts()),
    ]


def test_default_summarizes_all_signals():
    summary = summarize_signals_for_handoff(_signals())
    assert summary.signal_count == 4
    assert summary.highest_severity == "critical"
    assert summary.owners == ("docs", "platform", "qa", "release")


def test_min_severity_excludes_lower_signals():
    summary = summarize_signals_for_handoff(_signals(), min_severity="high")
    assert summary.signal_count == 2
    assert summary.highest_severity == "critical"
    assert summary.owners == ("platform", "release")


def test_min_severity_drops_owners_only_in_excluded_signals():
    summary = summarize_signals_for_handoff(_signals(), min_severity="critical")
    assert summary.signal_count == 1
    assert summary.owners == ("release",)


def test_fallback_owner_applies_to_surviving_blank_owner_signals():
    signals = [OperationSignal("handoff", "high", "   ", _ts())]
    summary = summarize_signals_for_handoff(
        signals, fallback_owner="engineering-ops", min_severity="high"
    )
    assert summary.owners == ("engineering-ops",)
    assert summary.signal_count == 1
