[Meta-Hacker-Cup](../../../) / [2020](../../) / [Round 3](../) / A. Chain Explosions

# A. Chain Explosions

Logan wants a connected dynamite network of at most 2000 sticks and at most 2000 fuse wires, numbered 1..N and 1..M. Each wire joins two different sticks, no unordered pair of sticks is wired twice, and the network must be connected.

A potential chain explosion is an ordered triple (a, b, c) of distinct sticks where a is wired to b and b is wired to c. Build any network with exactly K potential chain explosions. K is even, any valid network is accepted, and at least one exists for every legal K.

## Approach

Every chain explosion has exactly one middle stick, so grouping the triples by their middle partitions all of them. A stick of degree d can be the middle in d choices for a and d - 1 for c, so:

    total chain explosions = sum over all sticks v of deg(v) * (deg(v) - 1)

Only the degrees matter, never the wiring. The task therefore splits cleanly into choosing a degree sequence that adds up to K, then realizing it as one connected tree.

A star centre of degree d contributes d * (d - 1) and its leaves contribute nothing, which is a price list of 2, 6, 12, 20, 30, ... Precompute d * (d - 1) for d up to 2000 and repeatedly buy the largest price that fits, subtracting it from K. After buying a degree d star the remainder is below 2d, so K shrinks as 2000000 -> 2018 -> 38 -> 8 -> 2 -> 0 and only a handful of centres are ever needed. A remainder of 2 is always payable, since 2 is itself a price, and K being even keeps the change-making exact.

The centres then have to be joined. An edge between two centres is free when each one gives up a leaf slot to make room, because its degree, and therefore its contribution, does not change. So the centres are chained in a path, each end spending one slot and each interior centre two:

    leaves(centre i) = a[i] - 1 at the two ends, a[i] - 2 in the middle

With n centres and sum(a) total requested degree, that leaves N = sum(a) - n + 2 sticks and M = N - 1 wires: a tree, so it is connected. Sticks 1..n are the centres, the leaves take the numbers after them, and the output prints the spine edges first, then each centre's leaves.

## Complexity

O(sqrt(K)) per case, which is the size of the printed network; the decomposition is a few binary searches over the 2000-entry price table. O(1) extra space beyond the output buffer. Across every even K up to 2,000,000 the largest network is N = 1478 at K = 1,997,896, well inside the 2000 limit.

## Time

~0.006 seconds.

Solved: 12 November 2026.

## Lessons

- The idea for this solution came about surprisingly easily, because I misread the problem. I didn't realize that this 'tree' had to be fully connected, so I just came up with having some number of stars to fulfill k chains. The chaining of stars came quite easily from that.
- The triples are ordered, so a stick of degree d owns d * (d - 1) of them, not the C(d, 2) an unordered reading gives. That is also why every contribution is even, and therefore why K is guaranteed even.
- One fat star is far more efficient than many small ones. The greedy step takes the largest affordable degree for that reason.
- K = 2 is one degree-2 centre with two leaves, 3 sticks. Two centres with one leaf each is a 4-stick path and scores 4, so a chain cannot start before K = 4.
- The largest affordable price is easy to find with `bisect_right(prices, K) - 1`, the largest degree whose price still fits under k.
