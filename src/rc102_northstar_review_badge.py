DEFAULT_REVIEW_REQUIRED = True


def _coerce_flag(value, default):
    if value is None:
        return default
    return bool(value)


def build_badge(payload, lane_defaults):
    needs_review = _coerce_flag(
        payload.get("needs_review"),
        lane_defaults.get("needs_review", DEFAULT_REVIEW_REQUIRED),
    )
    return {
        "tenant": payload["tenant"],
        "case_id": payload["case_id"],
        "lane": lane_defaults["lane"],
        "badge": "review" if needs_review else "clear",
        "needs_review": bool(needs_review),
        "artifact_stage": lane_defaults.get("artifact_stage", "rc102"),
        "rule_key": lane_defaults.get("rule_key", "unset"),
    }
