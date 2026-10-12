# A. Double Squares

Count the number of ways to represent N as a sum of two squares (order and sign ignored).

## Approach

For each query N, iterate `a` from 0 to `sqrt(N)`, compute `b^2 = N - a^2`, and check whether `b^2` is a perfect square. Stop when `a > b` to avoid counting each pair twice. Results are memoized with `functools.cache`.

## Complexity

O(sqrt(N)) per unique query, O(1) per repeated query.

## Time

~0.2 seconds (measured by the script's own timer over the full input file).

Solved: 12 October 2026.

## Lessons

- `math.isqrt` avoids floating-point precision issues when checking perfect squares.
- Breaking when `a > b` halves the search space and prevents double-counting.
- The initial approach was to precompute the entire set of squares that could sum to 2^31, but that would have been roughly 2 billion computations. The per-query O(sqrt(N)) approach with memoization turned out to be the better choice — the input dataset did not demand the precompute, and per-query work with caching was both simpler and faster in practice.