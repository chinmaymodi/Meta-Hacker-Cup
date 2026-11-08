[Meta-Hacker-Cup](../../../) / [2020](../../) / [Qualification Round](../) / A. Travel Restrictions

# A. Travel Restrictions

N countries are arranged in a fixed sequence and flights only run between adjacent countries: a flight exists from i to j if and only if |i - j| = 1, in both directions. Each country also imposes its own restrictions. If I_i = "N" then no flight may land in country i; if O_i = "N" then no flight may leave country i. An adjacent flight from i to j is allowed only when neither endpoint blocks it, so i -> i+1 needs O_i = "Y" and I_(i+1) = "Y", and i -> i-1 needs O_i = "Y" and I_(i-1) = "Y". Output the N x N matrix P where P[i][j] = "Y" if country i can reach country j using zero or more flights, and "N" otherwise. P[i][i] is always "Y".

## Approach

Because the only edges join neighbours, the set of countries reachable from i is a contiguous interval containing i. A step right from k to k+1 is possible only when O_k = "Y" and I_(k+1) = "Y", so the row is filled outward from the diagonal: keep writing "Y" and advancing while that pair holds, and stop at the first failing pair, since every country beyond it would have to cross the same blocked edge. The identical scan runs leftwards from i using O_k = "Y" and I_(k-1) = "Y".

No graph search or transitive closure is needed. A detour cannot bypass a blocked adjacent edge, so the first "N" on each side ends that direction permanently.

## Complexity

O(N^2) per test case. Each of the N rows expands at most N cells in each direction, and the output matrix is N x N.

## Time

~0.006 seconds.

Solved: 8 November 2026.

## Lessons

- Every boundary is tested once per row, so the same two string lookups repeat N times. Precomputing `right[k] = (O[k] == "Y" and I[k+1] == "Y")` and `left[k] = (O[k] == "Y" and I[k-1] == "Y")` once per test case would turn each row into a plain array scan for a better runtime. That is only a constant-factor win, since the matrix is N x N and O(N^2) is the floor anyway, and at N <= 50 the current ~0.006 seconds is fast enough.
