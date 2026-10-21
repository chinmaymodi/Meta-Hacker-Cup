[Meta-Hacker-Cup](../../../) / [2014](../../) / [Qualification Round](../) / B. Basketball Game

# B. Basketball Game

Given N players with a shot percentage and a height, draft them by shot percentage (higher first, taller breaks ties) into two teams from alternating draft numbers. Each team starts with its P lowest draft numbers on the field. Simulate M minutes of substitutions and print the 2P players on the field at the end, sorted by name.

## Approach

Sort the players once by shot percentage descending, then height descending. That order is the draft: the odd draft numbers form team 1 and the even draft numbers form team 2. The first P players of each team start on the field, and the rest are on the bench.

Keep two min-heaps per team. The active heap is keyed by `[time, +shot, +height]`, with the time stored negated, so the smallest entry is the player with the most minutes played, ties going to the lower shot percentage and then the shorter player. The bench heap is keyed by `[time, -shot, -height]`, so the smallest entry is the player with the fewest minutes played, ties going to the higher shot percentage and then the taller player. Flipping the signs when a player moves between heaps converts between the two orderings.

Each minute every active entry's time is decremented by one. Popping the active minimum gives the player who leaves; pushing him onto the bench with the signs flipped gives the correct bench key. Popping the bench minimum gives the player who enters; pushing him onto the active heap with the signs flipped restores the active key. Because the same constant is subtracted from every active key, the relative order is unchanged, so no rebuild is needed between minutes. When a team has exactly P players, the bench is empty and the swap reduces to the same player leaving and re-entering, which changes nothing.

The active heaps are built as `team[p-1::-1]`, which puts the worst player first. Without the reversal the slice stays best-first, and the heap property only holds when the array is ordered by the active key. The reversed slice is a valid min-heap before the first pop, and `heappush` and `heappop` keep it valid afterwards.

## Complexity

O(N log N + M log P) time and O(N) space.

## Time

~0.008 seconds.

Solved: 21 October 2026.

## Lessons

- The heap property must hold before the first `heappop`. Slicing the best-first sorted list and then flipping the signs left the active arrays in descending key order, so `heappop` returned `heap[0]`, the best player, instead of the minimum. Reversing the slice fixes the order once, and every later push and pop preserves it, so `heapify` is never needed.
- The test data is weak. The buggy version still got 29 of the 30 cases right. The first pop was only wrong among players tied on time, and in longer games the bench-least-time rule pulled the wrongly benched player back, so the rosters corrected themselves. Case 19 was the only case with M = 1, where the first pop is the final answer, so only that one short case caught the bug.
