[Meta-Hacker-Cup](../../../) / [2011](../../) / [Qualification Round](../) / B. Peg Game

# B. Peg Game

A ball is dropped into one of the holes at the top of a peg board. Each time it hits a peg it bounces left or right with equal probability; if the peg is missing it falls straight through; at the walls it bounces back. The win hole is at column K in the bottom row. Find which top hole gives the highest probability of the ball landing in the win hole, and output that probability.

## Approach

Backward DP. Seed the target hole with probability 1 and propagate upward: each position takes the average of the two positions below it (the two bounce outcomes), a missing peg passes the value straight down, and wall positions take the single bounce. The answer is the top-row position with the highest value.

## Complexity

O(rows * cols) per test case.

## Time

~0.3 seconds.

Solved: 13 October 2026.

## Lessons

- The missing-peg handling only copied the straight-through value when the position below already had a non-zero probability. If the ball could not reach it, the missing peg was treated as a normal peg and probabilities came out too high. Always copy the value straight down, even when it is zero.
- The right-wall edge check never fired because it used the exclusive upper bound of the range, so the rightmost position went through the normal bounce path and its probability was halved. Check `i == r - 2` instead of `i == r`.
- Python's `round()` and `f"{x:.6f}"` use banker's rounding (round-half-to-even), so an exact tie like 0.3828125 formats as 0.382812. The judge expects round-half-up (0.382813). Use `int(x * 1e6 + 0.5) / 1e6`.