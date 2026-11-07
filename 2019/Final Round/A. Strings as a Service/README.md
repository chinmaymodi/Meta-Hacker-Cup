[Meta-Hacker-Cup](../../../) / [2019](../../) / [Final Round](../) / A. Strings as a Service

# A. Strings as a Service

Carlos needs to tune a 1,000-string guitar using notes A through G so that exactly K distinct palindromic chords can be played. A chord is any contiguous subset of one or more strings. Two chords are distinct if they use different strings, even if the notes are the same. Output any non-empty string of length at most 1,000 with exactly K distinct palindromic chords.

## Approach

A string of n identical characters produces exactly n*(n+1)/2 palindromic substrings, because every substring of identical characters is a palindrome. Precompute all triangular numbers t_i = i*(i+1)/2 up to 100000. Greedily decompose K into triangular numbers: take the largest t_i <= K, append i copies of the next unused letter, subtract t_i from K, and repeat. Each block of identical letters is isolated by a new letter, so palindromic chords cannot span across blocks and the counts add exactly.

## Complexity

O(sqrt(K)) to decompose K into triangular numbers, O(K) total output length bounded by 1000. O(1) extra space.

## Time

~0.045 seconds.

Solved: 7 November 2026.
