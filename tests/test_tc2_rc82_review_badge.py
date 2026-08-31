from src.tc2_rc82_review_badge import build_review_badge


def test_camel_false_review_flag_is_clear():
    row = build_review_badge({
        "tenant_id": "northstar",
        "destination_id": "appeals",
        "case_id": "case-440",
        "needsReview": False,
    })
    assert row["badge"] == "clear"
