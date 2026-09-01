from src.coverage_review_tc2_partner_boundary import resolve_partner_value

def test_internal_value_is_preserved():
    assert resolve_partner_value({"requires_review": 0}) == 0

def test_absent_value_uses_default():
    assert resolve_partner_value({}) == 0
