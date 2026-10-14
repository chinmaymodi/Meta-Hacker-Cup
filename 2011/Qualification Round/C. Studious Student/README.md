[Meta-Hacker-Cup](../../../) / [2011](../../) / [Qualification Round](../) / C. Studious Student

# C. Studious Student

Given a set of words, concatenate them in some order to produce the lexicographically lowest possible string.

## Approach

Sort the words with the comparator `a + b < b + a` (word `a` comes before `b` iff concatenating `a` then `b` is smaller than `b` then `a`), then join. Plain lexicographic sort is not enough: when one word is a prefix of another, the shorter word is not always the better first choice. For example, `["b", "ba"]` sorts to `"bba"`, but `"bab"` is smaller.

## Complexity

O(M log M) comparisons per set, each comparison O(total string length).

## Time

~0.001 seconds.

Solved: 13 October 2026.

## Lessons

- Plain `sorted()` fails when one word is a prefix of another. The comparator `a + b < b + a` is the correct ordering, and it is transitive, so sorting by it works.
- With M <= 9, brute-forcing all M! permutations is also feasible, but the comparator sort is simpler.