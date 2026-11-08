[Meta-Hacker-Cup](../../../) / [2020](../../) / [Qualification Round](../) / B. Alchemy

# B. Alchemy

Edgar has N shards of a broken Philosopher's Stone arranged in a row, each coloured "A" or "B", with N odd and N >= 3. One ritual step picks three consecutive shards that are not all the same colour, removes them, and puts a single new shard in their place whose colour is the majority colour of the three. Repeat until one shard remains. Decide whether the row can be reduced to a single shard without ever triggering a rebound explosion.

## Approach

A legal triple always contains both colours, so each ritual step removes exactly one "A" and one "B". Only the majority shard survives, and the two minority shards are converted to energy. If the row starts with a shards of "A" and b shards of "B", then after k steps it holds a - k and b - k shards, so the difference a - b never changes.

Reducing N shards to one takes exactly k = (N - 1)/2 steps, so the surviving shard is "A" when a = k + 1 and b = k, and "B" when a = k and b = k + 1. Both cases say the same thing: the two colour counts must differ by exactly one, that is, |a - b| = 1, or equivalently |2a - N| = 1.

## Complexity

O(N) per test case for one counting pass over the row, O(1) extra space.

## Time

~0.003 seconds.

Solved: 9 November 2026.

## Lessons

- The count difference is an invariant, which collapses the whole search over fusion orders into a single test on the input string.
- With |a - b| = 1 the row holds at least two of the higher count and one of the lower count, until a single shard is left, and since both colours are present some adjacent pair differs, so the pair plus either neighbour is always a legal triple. Every fusion removes one A and one B, so the difference stays at one and the row must end on the majority colour.
- Only the counts matter, never the arrangement: `shard_string.count("A")` is the entire per-case computation.
- |2*a_count-total_size| is just a way of reducing string parses.
