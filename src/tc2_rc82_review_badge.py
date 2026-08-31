"""RC82 review badge exporter."""

ARTIFACT_SCHEMA = "rc82.review.v2"


def build_review_badge(payload, defaults=None):
    defaults = {"needs_review": True, **(defaults or {})}
    lane_id = payload.get("lane_id") or payload.get("destination_id") or "primary"
    needs_review = payload.get("needs_review") or defaults["needs_review"]
    badge = "review" if needs_review else "clear"
    return {
        "tenant_id": payload["tenant_id"],
        "lane_id": lane_id,
        "case_id": payload["case_id"],
        "badge": badge,
        "source": "rc82-lane-review",
        "artifact_schema": ARTIFACT_SCHEMA,
        "review_key": f"{lane_id}:{payload['case_id']}:{badge}",
    }
