[Meta-Hacker-Cup](../../../) / [2014](../../) / [Round 1](../) / A. Labelmaker

# A. Labelmaker

Given a sorted set of working letters and a 1-indexed rank N, return the N-th label in shortlex order: all one-letter labels in alphabetical order, then all two-letter labels, and so on.

## Approach

The labels are the positive integers written in bijective base `len(letters)`. Bijective base has digits `1..len(letters)` and no zero digit, so ordinary base conversion does not apply directly.

Build the label from least significant digit to most significant. Each step uses `n, idx = divmod(n - 1, len(letters))`. The `n - 1` shifts the digit range down to `0..len(letters) - 1`, which indexes the sorted letter list directly. Appending `letters[idx]` produces digits in reverse order, so reverse the result at the end.

Subtracting one only once per case is not enough. The shift has to happen at every digit, because the block boundaries also move.

## Complexity

O(k) time and O(k) space, where k is the length of the answer.

## Time

~0.001 seconds.

Solved: 22 October 2026.

## Lessons

- Shortlex labels are bijective base-`len(letters)` numbers, not ordinary base numbers. Ordinary base allows a zero digit and produces a different ordering at block boundaries.
- The `-1` belongs inside the digit loop. Applying it once before the loop shifts only the first digit and leaves the rest as ordinary base digits.
- The initial approach built the label left to right, finding the leading digit and exponent for each character. It was replaced with a decimal-to-binary style conversion that builds right to left, one `divmod` per digit. That removed the repeated exponent search and was faster and simpler.
