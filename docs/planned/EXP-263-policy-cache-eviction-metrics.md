# EXP-263 - policy-cache eviction metrics (placeholder)

Linear: https://linear.app/experttc/issue/EXP-263/emit-policy-cache-eviction-metrics-for-export-workers
Category: Feature | Priority: Medium

## Problem
Export workers reuse a policy cache keyed by workspace and policy version, but eviction behavior is invisible, making memory-growth investigations guesswork.

## Planned change (placeholder)
Emit structured metrics (hit/miss/eviction counters + current entry-count gauge) via the existing metrics path. Metric emission only - no change to caching or eviction logic. No production logic changed in this placeholder PR.
