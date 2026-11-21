[Meta-Hacker-Cup](../../../) / [2012](../../) / [Round 1](../) / C. Squished Status

# C. Squished Status

Count how many ways a digit string can be split into integers from 1 to M, with no leading zeroes, modulo 4207849484. Constraints: 2 <= M <= 255, 1 <= length <= 1000.

## Approach

Let `dp[k]` be the number of valid splittings of the first `k` characters. Set `dp[0] = 1`, since the empty prefix has one splitting. For each start `i` whose digit is not `'0'`, grow the integer `v` one digit at a time while `v <= M`, and add `dp[i]` to `dp[j+1]` for every valid end `j`. The answer is `dp[n]`.

A chunk starting with `'0'` is never a valid character code, so all such starts are skipped.

## Complexity

Since `M <= 255`, at most three digits are examined from any start, so each position does constant work. Time is O(L) per message and memory is O(L), where L is the compressed length.

## Time

~0.006 seconds.

Solved: 21 November 2026.

## Lessons

- `dp[0]` must be 1. That was an easy to spot and fix mistake.
- The array needs length `L+1` and the scan must reach `j+1 == L`.
- Zero and leading-zero chunks need an explicit guard. `int("0")` is 0, outside `[1, M]`, and `int("01")` is 1 but has a leading zero. Case (`M=2`, `"101"`) is 0 only with that guard.
- The input is in a very poor format. `All tokens in the input will be separated by some whitespace.`, and as is evident from the sample, can mean spaces or newlines. So utilizing the `List.extend()` method is very nice in python.
- Apply the modulo at every addition. Counts for 1000-digit messages grow far beyond 64-bit.