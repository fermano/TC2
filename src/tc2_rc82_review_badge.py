"""Prototype review badge normalizer from before RC82 lane rows."""


def _needs_review(payload, default=True):
    if "needs_review" in payload and payload["needs_review"] is not None:
        return bool(payload["needs_review"])
    if "needsReview" in payload and payload["needsReview"] is not None:
        return bool(payload["needsReview"])
    return default


def build_review_badge(payload, defaults=None):
    defaults = {"needs_review": True, **(defaults or {})}
    needs_review = _needs_review(payload, defaults["needs_review"])
    return {
        "tenant_id": payload["tenant_id"],
        "destination_id": payload.get("destination_id") or payload.get("lane_id") or "primary",
        "case_id": payload["case_id"],
        "badge": "review" if needs_review else "clear",
        "source": "mainline-review-normalizer",
    }
