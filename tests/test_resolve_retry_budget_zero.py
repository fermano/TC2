from src.intake_service import resolve_retry_budget


def test_explicit_zero_is_honored():
    assert resolve_retry_budget(0, 3) == 0


def test_none_falls_back_to_default():
    assert resolve_retry_budget(None, 3) == 3


def test_positive_value_overrides_default():
    assert resolve_retry_budget(2, 3) == 2
