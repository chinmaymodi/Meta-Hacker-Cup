[Meta-Hacker-Cup](../../../) / [2018](../../) / [Qualification Round](../) / A. Tourist

# A. Tourist

Alex visits attractions in a repeating cycle: attraction 1, 2, ..., N, then back to 1, 2, ..., N, and so on. On each visit he sees exactly K attractions - the next K in the cycle. Given V-1 visits already made, determine which K attractions he sees on his Vth visit, output in decreasing order of popularity (original input order).

## Approach

The infinite visit sequence is `1, 2, ..., N, 1, 2, ..., N, ...`. On visit V, Alex sees positions `K*(V-1)+1` through `K*V` in that sequence. Map each position back to an attraction index modulo N, then sort the selected indices ascending to output in popularity order.

## Complexity

O(N) time per test case.

## Time

~0.003 seconds.

Solved: 27 October 2026.

## Lessons

- The visit pattern repeats every N attractions; use modulus to wrap indices.
- Output must be sorted by popularity (ascending index), not by visit order.
- V can be up to 1e12 but only `(V-1)*K % N` matters, so modulus keeps it small.
