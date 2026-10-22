[Meta-Hacker-Cup](../../../) / [2014](../../) / [Qualification Round](../) / C. Tennison

# C. Tennison

Given `K`, the probability Tennison wins a game when it is sunny or rainy, the initial probability of sun, and the probabilities and sizes of the sun-probability changes after a win or loss, return the probability that he wins the match.

## Approach

Let `F(w, l, p)` be the probability that Tennison wins the match given `w` wins, `l` losses, and current sun probability `p`. The answer is `F(0, 0, pi)`.

The base cases are `F(K, l, p) = 1` and `F(w, K, p) = 0`.

For every game there are eight outcomes: sunny or rainy, win or loss, and the sun probability goes up, down, or stays. The official recurrence sums all eight terms.

The sun probability is stored as an integer from `0` to `1000`, because the inputs are given to three decimal places. Only `p` and the two change amounts are scaled. The win probabilities and change probabilities stay as floats from `0.0` to `1.0`. Clamp `p` to `[0, 1000]` after every change.

The eight terms collapse to four because the weather only affects the win or loss probability. Let `win = p * ps + (1 - p) * pr` and `lose = 1 - win`. The up and down probabilities are the same in both weather branches, so the four recursive calls are:

- win, sun probability goes up
- win, sun probability stays
- loss, sun probability goes down
- loss, sun probability stays

For each test case, precompute the four branch coefficients and the clamped next `p` values for every `p` from `0` to `1000`. Then compute the reachable states bottom-up. Build the set of reachable `p` values for each `(w, l)` pair, and fill a DP table backward from the terminal rows. This computes only states that can actually occur and avoids recursion. Run the test cases in a process pool with six workers.

## Complexity

O(K^2 * 1001) time and space per case in the worst case, with O(1) work per reachable state. Only reachable `p` values are stored, so the actual table is usually smaller. The precomputed tables use O(1001) space per case. Six cases run in parallel.

## Time

~6 seconds.

Solved: 22 October 2026.

## Lessons

- The official 2014 solution used `1000` scaling to make `p` an integer memoization key. It was not necessary to scale `ps`, `pr`, `pw`, or `pl`. Scaling all of them and dividing by `1000` inside every state added work without changing the result.
- The first correct implementation of the official eight-term recurrence took about 78 seconds on the full input and 0.89 seconds on the sample. It made eight recursive calls per state and read all per-case values as globals.
- The first improvement grouped sunny and rainy branches with the same next state, reducing eight recursive calls to four. That version took about 52.5 seconds on the full input and 0.62 seconds on the sample.
- The precomputed recursive version precomputes the four coefficients and the two clamped `p` transitions for all 1001 values, and defines a fresh cached function for each test case. It ran in roughly 33 to 55 seconds on the full input and about 0.40 seconds on the sample. The earlier `Time` line used 40 seconds as a representative value.
- Converting the recursion to an iterative reachable-state DP reduced the full input to about 17 seconds in one process.
- Running cases in a process pool with six workers reduced the full input to about 6 seconds under normal load. The fastest observed run was 5.886 seconds; slower runs were caused by thermal and background load. Twelve workers were slower than six on a 6-core, 12-thread CPU because of SMT contention and lower all-core boost.
- The optimization timeline after the ~40-second recursive version was: multiprocessing alone at ~11.6 seconds with 12 workers, iterative DP alone at ~17.1 seconds, then the two combined with 6 workers for a sub-10-second run.
- The earlier recursive version could not share its cache across test cases. The iterative version avoids that problem because each case owns its own reachable-state table.
- The runtime is dominated by the number of reachable `(w, l, p)` states, not by the per-state arithmetic. Further single-process speedups are limited without changing the state representation or running cases in parallel.
