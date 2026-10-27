[Meta-Hacker-Cup](../../../) / [2018](../../) / [Qualification Round](../) / B. Interception

# B. Interception

Given an N-degree polynomial with reversed precedence (+ > * > ^, right-associative), find the number of distinct real x-intercepts.

## Approach

With `+` having the highest precedence, `*` middle, and `^` lowest (right-associative), the polynomial collapses to a power tower:

$$a^{b^{c^{\cdot^{\cdot^{\cdot}}}}}$$

Since `P_N != 0`, the base `P_N * x` can only be 0 when `x = 0`. For any `x != 0`, the result is nonzero -> no x-intercept.

At `x = 0`, every `h_i = P_i * x = 0`, giving a tower of `N+1` zeros:

$$0^{0^{0^{\cdot^{\cdot^{\cdot^{0}}}}}}$$

This alternates between 1 and 0:
- Innermost `0^0 = 1`, then `0^1 = 0`, then `0^0 = 1`, ...

- **N odd**: exponent tower = 1 -> `0^1 = 0` -> **K = 1** (x-intercept at `x = 0`)
- **N even**: exponent tower = 0 -> `0^0 = 1` -> **K = 0** (no x-intercept)

For example,
- N=0: `0^0 = 1` -> K=0 (even)
- N=1: `0^(0^0) = 0^1 = 0` -> K=1 (odd)
- N=2: `0^(0^(0^0)) = 0^(0^1) = 0^0 = 1` -> K=0 (even)

So odd N -> x-intercept at `x = 0`, even N -> none.

## Complexity

O(1) per test case - only need to check if N is odd.

## Time

~0.003 seconds.

Solved: 28 October 2026.

## Lessons

- Reversed precedence collapses the polynomial to a power tower of zeros at x=0.
- `0^0 = 1` by definition in this problem.
- The tower alternates 1, 0, 1, 0... so odd degree -> x-intercept exists, even degree -> none.
- x != 0 can never be a solution since P_N != 0 makes the base nonzero.
