[Meta-Hacker-Cup](../../../) / [2011](../../) / [Round 1B](../) / A. Chess 2

# A. Chess 2

Count the number of threatened pieces on a 16x16 Chess 2 board. A piece is threatened if another piece can move into its cell and take it. The board includes standard pieces (King, Queen, Rook, Bishop, Knight) plus Chess 2 additions: Nightrider (S), Archbishop (A), and Kraken (E). The Kraken can move to any square on the board regardless of obstacles, but does not threaten itself.

## Approach

For each piece, compute the set of squares it threatens based on its movement rules. Sliding pieces (Queen, Rook, Bishop, Archbishop, Nightrider) extend in straight lines or L-shapes until blocked by another piece or the board edge. The Knight and Archbishop use fixed-offset patterns. The Kraken threatens all occupied squares except its own position. The answer is the size of the union of all threatened-square sets.

## Complexity

O(P) per test case, where P <= 64. For each piece we check at most 64 tiles (e.g., a queen at the center scans ~8 tiles in each of 8 directions).

## Time

~0.02 seconds.

Solved: 14 October 2026.

## Lessons

This problem was pretty straightforward.
