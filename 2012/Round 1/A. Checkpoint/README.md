[Meta-Hacker-Cup](../../../) / [2012](../../) / [Round 1](../) / A. Checkpoint

# A. Checkpoint

Given $S$, find the shortest monotone right/up route from the origin to a goal that passes through a checkpoint and has exactly $S$ shortest paths. Constraints: $5 \le R \le 20$, $1 \le S \le 10^7$.

## Approach

There are $\binom{a+b}{a}$ monotone paths from $(0, 0)$ to $(a, b)$, and that segment is $a + b$ steps long. If the checkpoint splits the route into segments of lengths $A$ and $B$, then $S = \binom{A}{i} \cdot \binom{B}{j}$ and $T = A + B$. Write $L(v)$ for the shortest segment that gives exactly $v$ paths. The answer is $\min_{d \mid S} \left( L(d) + L(S/d) \right)$.

Since $\binom{v}{1} = v$, every $v$ is reachable in $v$ steps, with $1$ step in one direction and $v - 1$ in the other. So $L(v) \le v$, and a missing table entry simply uses $v$. Only cases where $k \ge 2$ saves steps need storing; the cheapest of those in row $n$ is $\binom{n}{2}$. That leaves 9,462 entries. Each test case walks divisors up to $\sqrt{S}$ and takes the smallest sum.

## Complexity

Precompute touches about 50,000 binomial cells. Each test case checks divisors up to $\sqrt{S}$, at most 3,163 for $S = 10^7$. Memory is $O(V)$ for the $V = 9{,}462$ table entries.

## Time

~0.019 seconds.

Solved: 20 November 2026.

## Lessons

- The fallback is not an edge case. I first gated on table membership, and prime $S$ values just printed the sentinel. Every integer is reachable through $\binom{v}{1} = v$, so a value missing from the table still has a length.
- The checkpoint cannot sit on the origin or the goal. Starting at $n = 0$ records $\binom{0}{0} = 1$ with length 0, which produced $S = 5 \to 5$ and $S = 1 \to 0$ instead of 6 and 2.

The table bounds all follow from $\binom{n}{2} \le 10^7$: that holds through $n = 4472$ and fails at 4473, so no later row can shorten an in-range value. Within a row, $\binom{n}{k} = \binom{n}{n-k}$ means $k$ only needs to reach $\lfloor n/2 \rfloor$, and the coefficients grow toward the middle, so once a value passes $10^7$ the rest of that half-row can be skipped. Start at $n = 1$ so $L(1) = 1$, and keep the first hit since $n$ increases and that is already the minimum length. That gives 9,462 entries in about 12 ms.
