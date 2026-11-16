[Meta-Hacker-Cup](../../../) / [2011](../../) / [Round 1C](../) / C. Risky Slide

# C. Risky Slide

A rectangular floor is tiled and nothing stands on it. Every tile has a stickiness rating from 1 to 9. You start at the edge of the floor and run in a straight line parallel to one wall, gaining the rating of every tile you cross as kinetic energy. At some tile boundary you switch to sliding in the same direction, and every tile you slide over costs its rating in energy. If a tile would take you below zero you stop partway through it and that tile does not count. Find the largest number of whole tiles you can slide across, over every choice of row or column, direction, and switch point.

## Approach

A move is fully described by three choices: which line of the floor (one row or one column), which direction along it, and at which tile boundary the run becomes a slide. Nothing crosses between lines, so the problem separates into independent lines and the answer is the best single line.

Starting from a border cell is always the best choice. Energy only ever helps and the run itself has no cost, so starting flush against the edge and running a longer prefix can only raise the energy available for the slide. That removes the start position as a decision.

For one line of ratings `a[0..L-1]`, take prefix sums `p` with `p[0] = 0` and `p[i+1] = p[i] + a[i]`, so `p[i]` is the energy collected after running over the first `i` tiles. Switching to the slide at boundary `i` means:

- energy in hand is `p[i]`
- sliding from tile `i` to tile `j-1` costs `p[j] - p[i]`
- all of those tiles are traversed completely exactly when that cost does not exceed the energy

which rearranges to a single inequality:

```
p[j] <= 2 * p[i]
```

The score for that split is `j - i`, and the best split for the line takes the largest `j` that satisfies it. There is no total to compare against; each split has its own budget, and the slide is allowed to stop short of the opposite wall.

Every rating is at least 1, so `p` is strictly increasing and the largest valid `j` is found by binary search. Each line is solved once in each direction, and the columns are obtained by transposing the grid, which is what `zip(*grid)` does.

## Complexity

O(R\*C\*log max(R,C)) time: every row and every column is scanned twice, once in each direction, with one binary search per split point. Extra space is O(max(R,C)) for the prefix sums of one line, beyond the grid itself. The shipped input holds 51 cases, the largest a 50x50 grid, with 48,314 tiles in total.

## Time

~0.047 seconds.

Solved: 16 November 2026.
