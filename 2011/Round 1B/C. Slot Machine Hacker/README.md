[Meta-Hacker-Cup](../../../) / [2011](../../) / [Round 1B](../) / C. Slot Machine Hacker

# C. Slot Machine Hacker

Given a sequence of observations from a slot machine that uses a linear function, predict the next 10 values. The function is `secret = (secret * 5402147 + 54321) % 10000001` and the machine displays `secret % 1000`. If the sequence cannot be produced by this function, output "Wrong machine". If the next 10 values cannot be uniquely determined, output "Not enough observations".

## Approach

For each test case, find all possible raw secret values that could produce the second observation, given the first observation, then iteratively filter candidates using subsequent observations. The first step iterates over all values in `[0, 10000001)` where `s % 1000 == firstObs` (about 10,000 candidates). For each subsequent observation, apply the linear function to every candidate and keep only those whose next output matches the observation. Once the candidate set shrinks to exactly 1, predict the next 10 values by running the function forward. If the set becomes empty, the sequence is impossible. If observations run out and the set still has multiple candidates, there are not enough observations.

## Complexity

O(K * N) per test case, where K is the number of candidate secrets (~10,000 for the first step) and N is the number of observations (<= 100). The candidate set shrinks rapidly after each observation, so the effective cost is much lower in practice.

## Time

~0.106 seconds.

Solved: 15 October 2026.

## Lessons

We could have precalculated all `currentSecret -> nextSecret` transitions as a lookup table if necessary, but the runtime is short enough that we did not do it.
