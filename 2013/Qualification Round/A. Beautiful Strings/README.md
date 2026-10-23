[Meta-Hacker-Cup](../../../) / [2013](../../) / [Qualification Round](../) / A. Beautiful Strings

# A. Beautiful Strings

A string's beauty is the sum of its letters' beauties, where the most frequent letter is worth 26, the next most frequent 25, and so on down to 1; case is ignored and non-letters are ignored.

## Approach

Lowercase each line and count every character with `Counter`. Sort the counts in descending order, then walk the sorted list with a starting weight of 26. Skip characters outside `a` through `z`, and decrement the weight only when a letter is used. Giving the largest weights to the largest counts maximizes the total.

## Complexity

O(L + K log K) per test case, where L is the line length and K is the number of distinct characters. K can grow with L, so the general worst case is O(L log L). Hacker Cup input is ASCII, which bounds K at 128, so in practice the scan is O(L).

## Time

~0.003 seconds.

Solved: 23 October 2026.

## Lessons

- The greedy assignment is optimal by an exchange argument: if a more frequent letter had a smaller weight than a less frequent one, swapping the weights would increase the total.
- The code counts punctuation and spaces along with letters, then skips them during weighting. That is safe because skipped characters never decrement `beauty`, so they cannot change a letter's rank.
- At most 26 weights exist, so sorting the counts is cheap. The input scan and file I/O are the real cost.
- The sort is over every distinct character, not just letters. Filtering to `a` through `z` before counting would cap K at 26 and make the O(L) bound unconditional.
