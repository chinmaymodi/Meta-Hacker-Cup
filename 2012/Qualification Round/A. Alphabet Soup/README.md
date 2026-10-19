[Meta-Hacker-Cup](../../../) / [2012](../../) / [Qualification Round](../) / A. Alphabet Soup

# A. Alphabet Soup

Given a sentence, count how many times its letters can be used to spell HACKERCUP.

## Approach

Count the letters in each line and compare against the letters a single HACKERCUP needs (H, A, C, C, K, E, R, U, P). Every copy consumes one of each letter and two C's, so the number of copies is limited by the scarcest letter, which is `available // needed`. The answer is the smallest of those ratios. `Counter('HACKERCUP')` records the double C directly, and spaces never match a needed letter so they need no special handling.

## Complexity

O(L) per test case for a sentence of L characters.

## Time

~0.02 seconds.

Solved: 19 October 2026.

## Lessons

- HACKERCUP needs two C's, so the counts have to be kept with multiplicity. Checking only whether each letter is present would be wrong. The minimum of `available // needed` over the letters, with C counted twice, gives the correct number.
- Spaces and letters outside the word are counted but never selected by the minimum, so the sentence does not need any pre-filtering.
