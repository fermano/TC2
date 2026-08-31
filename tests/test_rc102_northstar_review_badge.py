from src.rc102_northstar_review_badge import build_badge


def test_partner_false_alias_clears_badge():
    badge = build_badge(
        {"tenant": "northstar", "case_id": "case-440", "needsReview": False},
        {"lane": "appeals", "needs_review": True, "rule_key": "ns-a"},
    )

    assert badge["badge"] == "clear"
    assert badge["needs_review"] is False
