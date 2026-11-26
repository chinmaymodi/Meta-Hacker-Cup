[Meta-Hacker-Cup](../../../) / [2022](../../) / [Qualification Round](../) / B1. Second Friend and B2. Second Second Friend

# B1. Second Friend and B2. Second Second Friend

B1 is the small version without rocks. B2 is the large version where cells may also contain rocks. In both, add trees to empty cells so that every tree in the final grid has at least two tree neighbours in the four directions. Rocks can never become trees. Print any valid final grid, or `Impossible`.

A single README covers both problems because the script solves both input files with the same code. B1 was uploaded and accepted. B2 has no upload available, but the B2 logic is implemented and this entry counts as both problems solved.

## Approach

Treat the non-rock cells as a grid graph. We need a set of tree cells containing every original tree, where every cell in the set has at least two neighbours in the set. The unique maximal such set is the 2-core of that graph.

Start by turning every empty cell into a tree, so the candidate set is as large as possible. Count, for each non-rock cell, how many of its four neighbours are non-rock. Put every cell with fewer than two non-rock neighbours into a removal queue. Then repeatedly pop a cell, turn it back into an empty cell, and decrement the neighbour counts of its non-rock neighbours. When a neighbour's count drops below two, queue it too. A `seen` set prevents a cell from being queued or decremented twice.

When the queue is empty, the remaining trees are exactly the 2-core. If any original tree was removed, no valid arrangement exists, because every valid arrangement must be contained in the 2-core. Otherwise the remaining grid is a valid answer.

A one-row or one-column scene is special because no cell can ever have two neighbours that are not at an endpoint chain. If such a scene already has a tree, it is impossible. If it has no tree, the empty grid is valid.

## Complexity

O(R*C) time and O(R*C) memory per test case.

## Time

~0.143 seconds.

This is the combined time for both input files in one run.

Solved: 26 November 2026.

## Lessons

- B1's base answer is very simple: if there is only one row or one column, return `Impossible` once a tree exists; otherwise replace every `.` with `^`. Every tree then has at least two neighbours.
- The B2 version needs more care because rocks split the grid. The removal loop is just the standard peeling process for a 2-core, applied only to non-rock cells.
- The maximal-first strategy is important. Starting from all possible trees and pruning only what cannot work is simpler than trying to grow a valid set from the original trees.
