[Meta-Hacker-Cup](../../../) / [2022](../../) / [Qualification Round](../) / A. Second Hands

# A. Second Hands

There are `N` parts, each with a style `S_i`, and two display cases. Each case can hold at most `K` parts. A case may not contain two different parts of the same style. Decide whether every part can be placed in one of the two cases.

## Approach

Only two cases exist, so a style that appears three or more times cannot be placed: two copies must go into different cases, and there is no third case for the next copy. Also, the two cases together hold at most `2K` parts, so `N > 2K` is impossible.

These two checks are also sufficient. Let `a` be the number of styles that appear exactly twice, and let `b` be the number of styles that appear once. Put the two copies of each repeated style into different cases. This uses `a` slots in each case. Every remaining style appears once and can go into either case. The remaining capacity is `K - a` per case, so `2(K - a)` slots in total. Since `b = N - 2a` and `N <= 2K`, we have `b <= 2(K - a)`, so the single parts fit.

The solution only needs to decide YES or NO, not construct the placement, so counting distinct styles and their frequencies is enough.

## Complexity

O(N) per test case to build the frequency table.

## Time

~0.002 seconds.

Solved: 25 November 2026.
