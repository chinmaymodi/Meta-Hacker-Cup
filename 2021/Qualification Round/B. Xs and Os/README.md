[Meta-Hacker-Cup](../../../) / [2021](../../) / [Qualification Round](../) / B. Xs and Os

# B. Xs and Os

An N by N board holds Xs, Os and empty cells, with equal numbers of Xs and Os, no winner yet and at least one empty cell. You may now place any number of extra Xs in empty cells in one move. Find the minimum number of Xs needed to immediately win by filling a whole row or column, and how many different sets of cells achieve that minimum. Print Impossible if no such move exists.

## Approach

A row or column can only be completed if it contains no O at all, and completing one takes exactly as many Xs as it has empty cells. So the minimum is the smallest empty-cell count over every row and column that is free of Os, and the answer is Impossible when every line holds an O.

Counting the sets is then a matter of collecting every O-free line whose empty count equals that minimum. Any line with more empties needs more than the minimum number of placements, so it cannot contribute a set.

Two such sets can only be the same set when the minimum is 1, since a single cell can be the only empty cell of its row and of its column at the same time. Every set of size 2 or more from different lines forces different cells. Storing the cells of each candidate line as a tuple in a set removes that double count, and both scan directions produce the tuples in ascending cell order, so row-derived and column-derived copies of the same set compare equal.

The scan itself is one pass over the rows as strings, testing `'O' in row` and collecting the cells of each usable row as `i*n + j`, then the same over the columns taken from `zip(*grid)` with the key written as `j*n + i`. Wrapping the whole solve in a function keeps the loops fast, as elsewhere in this repo.

## Complexity

O(N^2) per case for the two scans, plus at most 2N candidate tuples of length at most N, so O(N^2) time and space in the worst case. The sum of N across all cases is at most 2000 with N at most 50, so the whole input is about 100000 character tests.

## Time

~0.006 seconds.

Solved: 14 November 2026.
