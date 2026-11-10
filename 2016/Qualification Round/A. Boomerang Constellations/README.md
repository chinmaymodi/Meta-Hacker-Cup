[Meta-Hacker-Cup](../../../) / [2016](../../) / [Qualification Round](../) / A. Boomerang Constellations

# A. Boomerang Constellations

Given N points on a 2D plane, count the number of "boomerang constellations" - unordered triples of points (A, B, C) such that the distance from A to B equals the distance from A to C (B and C are distinct, order doesn't matter).

## Approach

O(N^2) per test case. Store coordinates in integer arrays, use a list of dicts indexed by star position, and count distance frequencies with dict.get instead of storing neighbor sets.

## Complexity

O(N^2) time and space per test case.

## Time

~45.278 seconds.

Solved: 25 October 2026.

## Lessons

- Original version with tuple keys and set storage took ~225 seconds.
- Switching to frequency counts instead of neighbor sets dropped it to ~151 seconds.
- Removing explicit `if dist in dict` checks brought it to ~111 seconds.
- Integer-indexed coordinate arrays with cached locals got it to ~78.239 seconds.
- Squared distances avoid floats entirely.
- Only the count per distance matters, not which stars are at that distance.
- Moving the hot loop into a function, with no change to the logic, took it from ~78.239 seconds to ~45.278 seconds, about 1.7x. Python reads and writes variables much faster inside a function than at file level, and this loop does little else.
