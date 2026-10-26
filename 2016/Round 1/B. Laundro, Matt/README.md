[Meta-Hacker-Cup](../../../) / [2016](../../) / [Round 1](../) / B. Laundro, Matt

# B. Laundro, Matt

L loads of laundry, N washers (each takes W_i minutes per load), M dryers (each takes D minutes per load). Each load must be washed then dried. Find the minimum time to finish all loads.

## Approach

Wash phase: greedy simulation using a binary search. The L-th smallest wash time T is found by binary searching the smallest t where sum of floor(t/W_i) reaches L. The full schedule is built by generating all k*W_i <= T and sorting.

Dry phase: the dryer recurrence g(j) = max(wash[j], g(j-M)) + D is solved with the closed-form chain: answer = max over u of (wash[L-1-u*M] + (u+1)*D). When M >= L, every load gets its own dryer, so the answer is simply T + D.

## Complexity

O(N log T + L log L) time per test case, where T is bounded by L*min(W). The binary search dominates for small L; the schedule sort dominates for large L.

## Time

~5.795 seconds (12 workers, binary search + sort + closed-form chain + M>=L shortcut).

Solved: 26 October 2026.

## Lessons

- Version 1 (heap merge + per-dryer loop): used a priority queue to merge N washer schedules, then simulated each dryer one-by-one with an availability array. ~165.608s single-threaded.
- Version 2 (heap merge + closed-form dryer chain): same heap merge for washing, but replaced the per-dryer loop with the closed-form chain formula, walking the dryer chain backwards from the last load (L-1, L-1-M, L-1-2M, ...). ~80.956s single-threaded.
- Version 3 (binary search + sort + per-dryer loop): binary search found the L-th wash time T, built the full schedule by generating all k*W_i <= T and sorting, then used the per-dryer loop for drying. ~52.069s single-threaded.
- Version 4 (binary search + sort + closed-form chain): same binary search and sort for washing, but used the closed-form chain for drying instead of the loop. ~27.181s single-threaded.
- Version 5 (binary search + sort + closed-form chain + M>=L shortcut): same as version 4, but skipped building the schedule when M >= L (every load gets its own dryer, answer = T + D). ~24.757s single-threaded.
- Version 6 (multiprocessing, 12 workers): version 5 with ProcessPoolExecutor(max_workers=12, chunksize=1), bringing the full input solve time down to ~5.795 seconds.
