[Meta-Hacker-Cup](../../../) / [2014](../../) / [Qualification Round](../) / A. Square Detector

# A. Square Detector

Given an N x N grid of '.' and '#', decide whether the '#' cells form a single filled square aligned with the grid.

## Approach

Scan the grid once per case and track the bounding box of the '#' cells (minimum and maximum row and column) together with their total count. The '#' cells form a square exactly when the bounding box is square, meaning its height and width are equal, and the count equals the box area. The count test rejects holes, where the box holds more cells than are filled, while the height and width test rejects rectangles and other shapes.

Sample case 3 is a hollow ring whose bounding box is square, so only the count rejects it. Sample case 4 has four filled rows in a grid five columns wide, so its bounding box is not square. Cases 1 and 5 are filled squares of different sizes and pass.

## Complexity

O(N^2) per test case, with O(1) extra space.

## Time

~0.003 seconds.

Solved: 21 October 2026.

## Lessons

- A bounding box is not a square detector by itself. A hollow ring and a rectangle both have plausible bounds, so only the filled-cell count rules them out.
- The sentinel bounds start at `min = N` and `max = 0` and assume at least one '#'. A 1x1 grid with no '#' collapses to a 0x0 box and passes, so `count > 0` would be the safe guard. The contest input contained no empty grid.
