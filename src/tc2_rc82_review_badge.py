"""RC82 review badge exporter."""


def _flag(payload, name, default):
    if name in payload and payload[name] is not None:
        return bool(payload[name])
    return default


def build_review_badge(payload, defaults=None):
    defaults = {"needs_review": True, **(defaults or {})}
    lane_id = payload.get("lane_id") or payload.get("destination_id") or "primary"
    needs_review = _flag(payload, "needs_review", defaults["needs_review"])
    return {
        "tenant_id": payload["tenant_id"],
        "lane_id": lane_id,
        "case_id": payload["case_id"],
        "badge": "review" if needs_review else "clear",
        "source": "rc82-lane-review",
    }
