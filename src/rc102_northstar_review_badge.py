DEFAULT_REVIEW_REQUIRED = True


def _pick_review_flag(payload):
    for name in ("needs_review", "needsReview"):
        if name in payload and payload[name] is not None:
            return payload[name]
    return None


def _coerce_flag(value, default):
    if value is None:
        return default
    if isinstance(value, str):
        return value.strip().lower() not in {"false", "0", "no"}
    return bool(value)


def build_badge(payload, lane_defaults):
    needs_review = _coerce_flag(
        _pick_review_flag(payload),
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
        "release_channel": lane_defaults.get("release_channel", "candidate"),
    }
