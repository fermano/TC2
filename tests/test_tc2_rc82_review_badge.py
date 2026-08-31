from src.tc2_rc82_review_badge import ARTIFACT_SCHEMA, build_review_badge


def test_review_badge_uses_lane_shape():
    row = build_review_badge({
        "tenant_id": "northstar",
        "lane_id": "appeals",
        "case_id": "case-440",
        "needs_review": True,
    })
    assert row["lane_id"] == "appeals"
    assert row["badge"] == "review"
    assert row["source"] == "rc82-lane-review"
    assert row["artifact_schema"] == ARTIFACT_SCHEMA
    assert row["review_key"] == "appeals:case-440:review"


def test_defaults_to_review_when_flag_missing():
    row = build_review_badge({"tenant_id": "northstar", "lane_id": "ops", "case_id": "case-017"})
    assert row["badge"] == "review"
