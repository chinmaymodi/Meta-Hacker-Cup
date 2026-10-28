[Meta-Hacker-Cup](../../../) / [2018](../../) / [Qualification Round](../) / C. Ethan Searches for a String

# C. Ethan Searches for a String

Given string A, find string B such that Ethan's buggy `contains()` returns false even though A is a substring of B. If impossible, output "Impossible".

## Approach

Ethan's algorithm resets the pattern index to 1 on mismatch after a partial match, but does not advance the text index. This causes it to miss valid substrings in certain cases.

The key insight: construct B = A[:i] + A for some i where `i > 0` (i is not the first character), `A[i] == A[0]`, and `A[:i] + A[:-i] != A`. The string B contains A as a substring starting at position i, but Ethan's algorithm fails to find it because:

1. It matches A[:i] against B[:i] successfully.
2. At position i, B contains A[0] which matches A[i] (by our condition).
3. The partial match then fails later, Ethan resets to i=1 without advancing j, and gets stuck in a loop that never reaches the real match at position i.

Important caveat: if the **first** position i where `A[i] == A[0]` satisfies `A[:i] + A[:-i] == A`, then **all** subsequent positions also satisfy it. This is because A is periodic at that point - repeating the same block. So if the first match fails the condition, it's Impossible for all positions.

Example: `FBFBF` - at i=2, `A[:2]+A[:-2]` = `FB`+`FBF` = `FBFBF` = A, so Impossible.

If no such i exists, output "Impossible".

## Complexity

O(N) per test case - the `break` after finding the first `i` where `A[i] == A[0]` means each case does one slice/compare at most.

## Time

~0.004 seconds.

Solved: 28 October 2026.

## Lessons

- Ethan's algorithm restarts pattern matching from i=1 but keeps j advanced, missing certain substrings.
- Construct B = A[:i] + A where i is the first position (>0) with A[i]==A[0] and A[:i]+A[:-i] != A.
- If the first such i satisfies A[:i]+A[:-i] == A, then all subsequent positions do too (A is periodic) - so it's Impossible.
