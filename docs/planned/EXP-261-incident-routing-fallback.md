# EXP-261 - Incident routing silent fallback (placeholder)

Linear: https://linear.app/experttc/issue/EXP-261/incident-routing-silently-falls-back-to-default-owner-when
Category: Bug | Priority: High

## Problem
When config/operations.yml has no incident-routing entry for a team, the service silently routes the incident to the global fallback owner with no warning, so the intended team's on-call is never paged.

## Planned change (placeholder)
Make a missing routing key observable: emit a WARNING log and mark the routing result as `unrouted` instead of silently substituting the fallback owner. No production logic is changed in this placeholder PR.

## Decision
Resolved via PR review / EXP-261: adopt option (b) - fail-open with a WARNING log plus an explicit `unrouted` marker on the routing result. Hard-failing at config load (option (a)) is explicitly rejected, to avoid taking the service down over a single bad team entry.
