from src.rc102_northstar_review_badge import build_badge


def test_absent_badge_inherits_review_default():
    badge = build_badge(
        {"tenant": "northstar", "case_id": "case-440"},
        {
            "lane": "appeals",
            "needs_review": True,
            "artifact_stage": "candidate",
            "rule_key": "ns-a",
            "release_channel": "rc102-final",
        },
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


def test_snake_false_clears_review_badge():
    badge = build_badge(
        {"tenant": "northstar", "case_id": "case-442", "needs_review": False},
        {"lane": "appeals", "needs_review": True, "rule_key": "ns-a"},
    )

    assert badge["badge"] == "clear"
    assert badge["needs_review"] is False
    assert badge["rule_key"] == "ns-a"


def test_partner_false_alias_clears_e04_badge_without_dropping_release_metadata():
    badge = build_badge(
        {"tenant": "northstar", "case_id": "case-440", "needsReview": False},
        {
            "lane": "appeals",
            "needs_review": True,
            "artifact_stage": "candidate",
            "rule_key": "ns-a",
            "release_channel": "rc102-final",
        },
    )

    assert badge == {
        "tenant": "northstar",
        "case_id": "case-440",
        "lane": "appeals",
        "badge": "clear",
        "needs_review": False,
        "artifact_stage": "candidate",
        "rule_key": "ns-a",
        "release_channel": "rc102-final",
    }


def test_canonical_flag_wins_during_alias_overlap():
    badge = build_badge(
        {
            "tenant": "northstar",
            "case_id": "case-443",
            "needs_review": False,
            "needsReview": True,
        },
        {"lane": "appeals", "needs_review": True},
    )

    assert badge["badge"] == "clear"
    assert badge["needs_review"] is False


def test_partner_false_like_string_clears_badge():
    badge = build_badge(
        {"tenant": "northstar", "case_id": "case-444", "needsReview": "false"},
        {"lane": "appeals", "needs_review": True},
    )

    assert badge["badge"] == "clear"
    assert badge["needs_review"] is False
