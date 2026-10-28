[Meta-Hacker-Cup](../../../) / [2018](../../) / [Round 1](../) / A. Let It Flow

# A. Let It Flow

Count valid pipe configurations in a 3xN grid where water flows from top-left to bottom-right using elbow-shaped pipes.

## Approach

Dynamic programming by column. `dp0`, `dp1`, `dp2` = number of ways water reaches rows 0, 1, 2 at current column. For each column, transitions depend on whether current and previous cells are blocked:

- Row 0: `n0 = dp1` (comes from row 1)
- Row 1: `n1 = dp0 + dp2` (comes from row 0 or row 2)
- Row 2: `n2 = dp1` (comes from row 1)

Only cells where both previous and current cell are `.` allow flow. Answer is `dp1 % MOD` (water exits bottom-right at row 1, last column).

## Complexity

O(N) time per test case - single pass through N columns with 3 states. Optimal since all input must be read.

## Time

~0.088 seconds.

Solved: 28 October 2026.

## Lessons

- Initial code runtime was ~0.117 seconds.
- Using individual variables instead of a dp[] list and early exit on a [0,0,0] state took it down to ~0.104 seconds.
- Precomputing column passability arrays (`can0`, `can1`, `can2`) to remove string indexing from the hot loop, took it down to ~0.096 seconds.
- Finally, only doing modulo on `a+c` instead of all 3 dp variables, took it down to ~0.088s.
- The goal was to reach a sub 0.1 second runtime which made me happy.
