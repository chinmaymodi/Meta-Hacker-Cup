[Meta-Hacker-Cup](../../../) / [2025](../../) / [Round 1](../) / A1. Snake Scales (Chapter 1)

# A1. Snake Scales (Chapter 1)

Solid Snake starts on platform 1 and has to visit every platform. Platform `i` is the horizontal segment from `(i, A_i)` to `(i+1, A_i)`, and he carries one ladder. A ladder of height `h` can connect two platforms when a vertical segment of length `h` touches both. Find the height of the shortest ladder that lets him visit every platform.

## Approach

The ground cannot be used, so Snake can only move between adjacent platforms. Platforms `i` and `i+1` meet at `x = i + 1`, where their heights are `A_i` and `A_{i+1}`, so crossing that boundary needs a ladder of height `|A_i - A_{i+1}|`. Every boundary from `1` to `N - 1` has to be crossed and the same ladder has to cover all of them, so the answer is the largest adjacent difference. A single platform has nothing to cross, so the answer is 0.

## Complexity

O(N) per test case.

## Time

~0.001 seconds.

Solved: 21 October 2026.

## Lessons

- The ladder is bought once, so the answer is the maximum adjacent gap, not the sum. This is a minimax bottleneck along a path.
- `N = 1` is the only case that returns 0. The general maximum over an empty set of differences would fail, so it needs its own branch.
- The `N = 1` branch still reads the platform line before appending 0. Skipping the read would leave the file cursor on the next case's `N`.
