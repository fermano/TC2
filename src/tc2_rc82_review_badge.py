"""RC82 review badge exporter."""


def build_review_badge(payload, defaults=None):
    defaults = {"needs_review": True, **(defaults or {})}
    lane_id = payload.get("lane_id") or payload.get("destination_id") or "primary"
    needs_review = payload.get("needs_review") or defaults["needs_review"]
    return {
        "tenant_id": payload["tenant_id"],
        "lane_id": lane_id,
        "case_id": payload["case_id"],
        "badge": "review" if needs_review else "clear",
        "source": "rc82-lane-review",
    }
