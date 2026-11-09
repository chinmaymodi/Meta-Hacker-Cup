[Meta-Hacker-Cup](../../../) / [2020](../../) / [Qualification Round](../) / C. Timber

# C. Timber

A line of trees stands at given positions, each with a height. Every tree falls either left or right, and a fallen tree covers the interval from its stump to the tip in its fall direction. Trees knocked over by a falling tree fall in the same direction. Choose a fall direction for each tree to maximize the length of the longest contiguous interval of fallen trees.

## Approach

Sort the trees by position. Sweep left to right assuming every tree falls right, tracking how far each contiguous right-falling chain reaches using a map from landing position to chain length. Then sweep right to left assuming every tree falls left, similarly tracking left-falling chains. For each tree, consider falling it right (chain ending at its position plus its own height) and falling it left (a left chain reaching it plus a right chain starting from its position), and keep the global maximum. Each sweep is one pass over the sorted trees with O(1) map operations per tree.

## Complexity

O(N log N) per test case for the sort, O(N) for the two sweeps, O(N) extra space for the maps.

## Time

~9.4 seconds.

Solved: 10 November 2026.

## Lessons

- Sorting by position is what makes the linear sweeps valid: a tree can only be reached by its immediate neighbours in position order.
- The map keyed by final fall position lets a chain "announce" how far it reaches so a later tree can pick it up in O(1).
- Running the sweep twice (all-right, then all-left) and combining at each tree covers the mixed-direction cases without enumerating every direction assignment.
