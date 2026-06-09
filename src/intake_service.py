"""Helpers used by support intake and release coordination paths."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TypedDict


_SEVERITY_RANK = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4,
}


class HandoffRow(TypedDict):
    owner: str
    severity: str
    summary: str


def resolve_retry_budget(requested: int | None, default: int) -> int:
    """Return the configured retry count unless a request overrides it."""
    return default if requested is None else requested


def filter_handoff_rows(
    rows: Iterable[HandoffRow],
    *,
    min_severity: str | None = None,
) -> list[HandoffRow]:
    """Return handoff rows in the order copied from support notes.

    When min_severity is set, keep only rows whose severity ranks at or
    above the threshold (low < medium < high < critical). Unknown severities
    rank lowest. Input order is always preserved.
    """
    ordered = list(rows)
    if min_severity is None:
        return ordered
    if min_severity not in _SEVERITY_RANK:
        raise ValueError(f"unknown minimum severity: {min_severity}")
    threshold = _SEVERITY_RANK.get(min_severity, 0)
    return [
        row for row in ordered if _SEVERITY_RANK.get(row["severity"], 0) >= threshold
    ]


def extract_release_marker(note: str) -> str:
    """Normalize surrounding whitespace for a release marker."""
    return note.strip()