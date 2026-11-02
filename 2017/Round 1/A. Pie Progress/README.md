[Meta-Hacker-Cup](../../../) / [2017](../../) / [Round 1](../) / A. Pie Progress

# A. Pie Progress

Every day for N days you eat one pie. On day i the shop sells M pies priced C[i][j], and you may buy any subset of them, including none. Pies do not expire, so a pie bought on an earlier day can be eaten later. Buying p pies on one day costs the sum of their prices plus p*p. Minimize the total cost.

## Approach

Sort each day's prices. Buying p pies on a day costs the p cheapest prices plus p*p, so the j-th pie bought that day adds `C_j + 2j - 1`, since the p*p term grows by 2p-1. Marginal costs inside a day strictly increase.

Keep one heap per day holding that day's unbought prices, and one global heap holding each day's current cheapest marginal cost. Each day, pop the global minimum and charge it, remove that pie from its day's heap, then push that day's next marginal cost. A day's j-th pie is strictly more expensive than its (j-1)-th and available at the same time, so it can never be taken first, which is why one candidate per day is enough.

## Complexity

O(N*M) to heapify every price, O(N log N) for the global heap, O(N log M) for the per-day removals. Space is O(N*M).

## Time

~0.205 seconds.

Solved: 3 November 2026.

## Lessons

- The first version sorted each day and pushed all M taxed pies into one heap, popping one per day. Correct, but only N of the N*M entries can ever be bought, so the heap reached N*M entries and every push paid log(N*M).
- A day's j-th pie is always more expensive than its (j-1)-th and appears at the same moment, so it can never win the global comparison early. That leaves only each day's head needing to compete.
- One heap per day plus a global heap of size N cut pushes from N*M to about 2N, and the log factor from log(N*M) to log(N).
- heapify instead of sort: only N/M pies per day are bought on average, so most of the sorted order was never used.
- Measured with the same harness on the same input: 0.51 seconds before, 0.20 seconds after, identical output.
