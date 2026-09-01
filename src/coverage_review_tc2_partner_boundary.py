def resolve_partner_value(payload, default=0):
    value = payload.get("requires_review")
    if value is None:
        value = payload.get("requiresReview")
    return default if value in (None, "") else value
