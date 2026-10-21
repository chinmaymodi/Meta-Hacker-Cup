[Meta-Hacker-Cup](../../../) / [2011](../../) / [Round 1B](../) / B. Diminishing Circle

# B. Diminishing Circle

N people stand in a circle. Starting from person 1, count K people clockwise, then the K+1-th person leaves the circle. The process repeats starting from the person clockwise of the last person removed. Find the winner (1-indexed position).

## Approach

This is the Josephus problem with step size K+1. Use the improved O(k log n) formula from Wikipedia for the general case. When n >= k, build a stack of intermediate values and compute the result by unwinding. When n < k, compute the standard Josephus recurrence iteratively. The step size is K+1 because we count K people and eliminate the next one.

## Complexity

O(n) per test case when n < k, O(k log n) when n >= k. The stack-based approach avoids deep recursion.

## Time

~0.9 seconds.

Solved: 16 October 2026.

## Lessons

- The step size is K+1, not K. Counting K people and eliminating the K+1-th means every (K+1)-th person is removed.
- Python's recursion limit is exceeded for large n (~15000+), so the iterative stack-based approach is necessary instead of the simple recursive formula.
- Multiprocessing and C extensions were considered but the process spawn overhead exceeds the computation time for only 60 test cases.
