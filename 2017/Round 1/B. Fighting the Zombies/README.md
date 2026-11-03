[Meta-Hacker-Cup](../../../) / [2017](../../) / [Round 1](../) / B. Fighting the Zombies

# B. Fighting the Zombies

N zombies stand at integer coordinates on an infinite plane. Cast Move once: choose a center, a radius and a translation, and every zombie inside that circle is shifted by the translation. The radius may be any positive real. Then cast Destroy once: every zombie inside an axis-aligned square of side R is killed. Maximize the number of zombies killed.

## Approach

Move shifts every zombie it picks up by the same vector, so the picked-up zombies keep their relative positions. Destroy kills one R-square's worth. Take that square and a second R-square at the positions the moved zombies started from: a zombie inside the second square is translated into the first and dies, and a zombie already inside the first square dies whether or not it was moved. So the two spells kill exactly the zombies covered by the union of two R-squares.

Any group that fits in an R-square also fits in one whose left edge is the smallest x of the group and whose top edge is the largest y of the group, both coordinates of zombies. That leaves N*N candidate squares, anchored at (x_i, y_j) and extending R to the right and R downward.

Each square stores its members as a bitmask over zombie indices. The answer is the largest popcount of the OR of two masks, with a mask allowed to pair with itself for the case where one square is enough.

## Complexity

O(N^2) to build the axis masks, then O(M^2) over the M masks not contained in another. M is at most N^2, so the worst case is O(N^4). Space is O(N^2) masks.

## Time

~0.054 seconds.

Solved: 4 November 2026.

## Lessons

- Move preserves relative positions, which turns the two spells into the union of two R-squares. Moving a zombie whose original position is already inside the destroy square costs nothing.
- The anchor (x_i, y_j) takes its x from one zombie and its y from another, so the containment test has to read the anchor. The first version read the donor zombies' coordinates instead, which built plausible-looking squares that counted the wrong zombies.
- The anchor pair does not have to be two zombies that share a square. Two zombies can sit in one R-square while being up to R*sqrt(2) apart, so the necessary condition on an anchor pair is `dx^2 + dy^2 <= 2*R^2`. The first version applied the circle test from Move, `dx^2 + dy^2 <= R^2`, to the square anchors and discarded the squares that covered the most zombies.
- The pair loop has to include i == j. With `range(i+1, ...)` a single square is never scored, so a horde of one zombie answered 0.
- The R*sqrt(2) filter only removes redundant candidates: any square it drops covers a set that is also covered by the square anchored at that set's own leftmost and topmost zombie.
- Before these fixes, 8 of the 116 local cases were wrong: four from the pair loop and four from the circle test.
- Building every anchor first and filling the masks in a second pass over the squares, so each square's corner is unpacked once instead of rebuilt for every zombie, took the mean from ~0.548s to ~0.406 seconds.
- Collapsing duplicate masks, dropping every mask contained in another, and breaking out of the pair loop once the two popcounts cannot beat the best count found, took the mean from ~0.406s to ~0.154 seconds.
- Factoring the membership test into an x-window mask AND a y-window mask, so each zombie is tested against 2N windows instead of N*N corners and every square costs one AND, took the mean from ~0.154s to ~0.054 seconds.
- The same algorithm went from ~0.548s to ~0.054s, a factor of 10, which was great fun.
