[Meta-Hacker-Cup](../../../) / [2022](../../) / [Qualification Round](../) / D. Second Flight

# D. Second Flight

There are `N` airports and `M` undirected flight paths. Path `i` joins airports `A_i` and `B_i` and carries up to `C_i` tourists. Every morning two direct flights run on that path, one in each direction, and every evening another two run, again one in each direction. For each of `Q` days, given airports `X_i` and `Y_i`, report the maximum number of tourists who can fly from `X_i` to `Y_i`. A tourist may fly directly or take one morning flight followed by one evening flight through a shared intermediate airport.

Official input, output, and solution files: [Meta Hacker Cup 2022 Qualification Round downloads](https://www.dropbox.com/scl/fo/2558rp1lq5gl4wwedepn1/AP0HKMqPqmWqtybuKJ0FJaA?rlkey=9je8c49o1rvn1jbqe37e8vpsd&e=3&dl=0).

Constraints: `T <= 70`, `N, M, Q <= 200000`, `C_i <= 1e9`, and the sum of `Q` over all cases is at most `5,000,000`. Every unordered pair `(A_i, B_i)` appears at most once in a case.

## Approach

Let `w(u,v)` be the capacity of the edge between `u` and `v`, or `0` if there is no edge. For a query `(X,Y)`:

```text
F(X,Y) = 2*w(X,Y) + SUM over k of min(w(X,k), w(Y,k))
```

The direct part is `2*w(X,Y)` because the morning direct flight and the evening direct flight are separate resources. A two-hop route through `k` uses a morning seat on `X -> k` and an evening seat on `k -> Y`, so it carries `min(w(X,k), w(Y,k))`.

The sum is a sum rather than a maximum because different intermediate airports use different flights. The morning seats out of `X` are all distinct, and the evening seats into `Y` are all distinct, so all two-hop routes can run simultaneously. The direct edge cannot also appear as one leg of a valid two-hop route, since the missing leg would have to be a self-loop.

Store the graph as an array of hash maps, one per airport, where `adj[u][v] = w(u,v)`. Each inner map holds only the neighbours of `u`, so memory is `O(N + M)` instead of the impossible `O(N^2)` of a full matrix.

For each query, swap endpoints if needed so the lower-degree airport is scanned. The answer is symmetric, so this does not change the value. Scan the smaller neighbour map and check each neighbour against the other endpoint with a single hash lookup. Terms where the other leg does not exist contribute zero.

Memoize answers by unordered query pair. Since the endpoints are canonicalized by `(degree, node)`, repeated questions in either direction reuse the same answer. The cache key is an integer packing `(x << 20) | y`, which is safe because node IDs are below `2^20`.

The input file has 80 cases, 4,625,236 edges and 4,979,212 queries. Fourteen cases have `(N, M, Q) = (200000, 200000, 200000)`, so avoiding the `Q*N` full scan is essential.

## Correctness

For a fixed query `(X,Y)`, a midpoint `k` contributes only if both `(X,k)` and `(k,Y)` exist. Scanning `adj[X]` visits every neighbour of `X`, and the hash lookup in `adj[Y]` skips exactly those `k` that are not also neighbours of `Y`. Therefore every common neighbour is visited once, and no other midpoint is considered.

For each common neighbour `k`, the code adds `min(w(X,k), w(Y,k))`, which is the capacity of the two-hop route through `k`. Adding `2*w(X,Y)` accounts for the two direct flights. These resources are disjoint across different `k` and separate from the direct flights, so the sum is the maximum possible number of tourists.

Swapping the endpoints does not change `min(w(X,k), w(Y,k))`, and the direct edge is symmetric, so scanning the lower-degree endpoint preserves the answer. Memoization is safe because the answer depends only on the unordered pair and the fixed graph for that case.

## Complexity

Building the adjacency maps takes `O(N + M)` time and memory per case.

For one distinct queried pair, the scan costs `O(min(deg(X), deg(Y)))` expected hash-map time. With degrees sorted as `d1 >= d2 >= ... >= dN`, the cost of pair `(i,j)` with `i < j` is `d_j`. Taking only the `Q` largest such terms needs only the first `O(sqrt(Q))` degree columns, and their total is bounded by `O(M*sqrt(Q))` because the sum of all degrees is `2M`.

Total per case is therefore `O(N + Q + M*sqrt(Q))` time and `O(N + M + Q)` memory. Hash-map operations are expected `O(1)`. With `M = Q = 200000`, the extra work is on the order of `9e7` neighbour visits instead of `4e10` naive checks.

## Time

~45 seconds.

This is the runtime for the full 118 MB input file. The output was compared byte-for-byte with `OFFICIAL_second_flight_output.txt` and matched exactly.

Solved: 28 November 2026.

## Lessons

- The two-hop part is a sum over common neighbours, not a maximum. Different intermediates use different seats, so their flows add.
- A full `N x N` capacity table is both impossible to allocate and unnecessary. An array of per-node hash maps stores only real edges.
- Orienting each query to the lower-degree endpoint is the key step. It turns `Q*N` into a bound driven by the degree distribution.
- Memoizing unordered pairs matters when the same query is repeated. The canonical key must agree with the orientation rule.
- Binding `adjacency_list[y].get` once per computed pair was the largest constant-factor win in Python. It removed a list index, attribute lookup, and method lookup from every neighbour iteration.
