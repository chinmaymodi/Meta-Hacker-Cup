[Meta-Hacker-Cup](../../../) / [2011](../../) / [Round 1A](../) / C. Wine Tasting

# C. Wine Tasting

G glasses hold G different wines, each labelled. After tasting, the labels are removed and the glasses are presented unlabelled. The taster guesses which wine is in each glass, giving a different wine for every glass, and wins if at least C guesses are correct. Count the number of winning guesses modulo 1051962371.

## Approach

A guess is a permutation of the G wines, and a correct guess is a fixed point of that permutation. The number of permutations of G elements with exactly k fixed points is the rencontres number T(G, k) (OEIS A008290), so the answer is a partial row sum:

```
sum_{k=C}^{G} T(G, k)
```

The whole triangle for n <= 100 is precomputed with the van Wijk recurrence, which uses only additions and multiplications:

```
T(n, k) = T(n-1, k)*(n-1-k) + T(n-1, k+1)*(k+1)                 for k = 0
T(n, k) = T(n-1, k-1) + T(n-1, k)*(n-1-k) + T(n-1, k+1)*(k+1)   for k >= 1
```

seeded by the base case T(0, 0) = 1. Every cell is reduced modulo 1051962371.

## Complexity

O(G^2) precomputation for G <= 100 (~5000 cells), then O(G) per test case to sum the row tail.

## Time

~0.01 seconds.

Solved: 17 October 2026.

## Lessons

- The first intuition was to count by wrong guesses: "at least C correct" is the same as "at most G-C wrong", i.e. exactly 0, 1, ..., G-C wrong. Exactly 0 wrong is 1 way, exactly 1 wrong is impossible, and exactly 2 wrong means choosing 2 glasses to swap, C(G,2) ways.
- Generalizing that led to the [Rencontres numbers](https://en.wikipedia.org/wiki/Rencontres_numbers) and [Derangement](https://en.wikipedia.org/wiki/Derangement) pages, and then to [OEIS A008290](https://oeis.org/A008290), which tabulates T(n, k), the number of permutations of n with exactly k fixed points.
- From A008290 we used the van Wijk formula to precompute the triangle. Even though this is a combinatorics problem, that recurrence turned it into a plain DP over a table, which was satisfying.
