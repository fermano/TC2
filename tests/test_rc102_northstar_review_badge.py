from src.rc102_northstar_review_badge import build_badge


def test_absent_badge_inherits_review_default():
    badge = build_badge(
        {"tenant": "northstar", "case_id": "case-440"},
        {"lane": "appeals", "needs_review": True, "artifact_stage": "candidate", "rule_key": "ns-a", "release_channel": "rc102-final"},
    )

    assert badge["badge"] == "review"
    assert badge["needs_review"] is True
    assert badge["artifact_stage"] == "candidate"
    assert badge["rule_key"] == "ns-a"
    assert badge["release_channel"] == "rc102-final"


def test_snake_true_keeps_review_badge():
    badge = build_badge(
        {"tenant": "northstar", "case_id": "case-441", "needs_review": True},
        {"lane": "appeals", "needs_review": False},
    )

    assert badge["badge"] == "review"
    assert badge["needs_review"] is True
    assert badge["release_channel"] == "candidate"
