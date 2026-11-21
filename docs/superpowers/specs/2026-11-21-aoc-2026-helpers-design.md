# AoC 2026 helper library — design

## Intent
Prepare a `2026/` folder before Advent of Code 2026 starts, with a `common.py`
helper module in the same style as previous years, so day solutions can
`from common import ...` from day one.

## Goals
- `2026/common.py` containing everything from `2025/common.py`, unchanged in
  name, signature and behavior.
- Add a small set of helpers for patterns repeatedly hand-written in past
  solutions.

## Non-goals / anti-goals
- No per-day template, no input auto-download, no session cookie handling.
- No package structure, third-party dependencies, or class-heavy design —
  plain functions with type hints, matching existing style.
- Don't change prior years' files.

## Constraints
- Solutions are run from the repo root with paths like `'2026/aoc_01.txt'`;
  `from common import ...` resolves because the script's directory is on
  `sys.path`.
- `*.txt` inputs are gitignored.
- Python standard library only.

## Approaches
1. Carry forward 2025's `common.py` only — zero effort, but recurring code stays duplicated.
2. **Carry forward + recurring helpers (chosen)** — small additions drawn from past code.
3. Larger toolkit (templates, auto-download) — rejected: beyond what was used before, needs a session cookie.

## Additions
- `ints(line) -> list[int]` — all integers (including negatives) in a string.
- `DIRS4`, `DIRS8` — `(drow, dcol)` direction tuples.
- `in_bounds(grid, row, col) -> bool`.
- `neighbors(grid, row, col, dirs=DIRS4)` — yields in-bounds `(row, col)`.
- `bfs(start, next_states) -> dict[state, distance]` — `next_states(state)` yields neighbor states.
- `dijkstra(start, next_states) -> dict[state, cost]` — `next_states(state)` yields `(neighbor, cost)`; uses `heapq`.

## Left to the builder
- Exact docstrings and small internal details.
- A quick test script (scratch, not committed) verifying each helper.
