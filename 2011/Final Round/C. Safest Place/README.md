[Meta-Hacker-Cup](../../../) / [2011](../../) / [Final Round](../) / C. Safest Place

# C. Safest Place

Find the integer point $p \in [0, 1000]^3$ maximizing the squared distance to its nearest bomb. There are $T = 50$ test cases and at most $N = 200$ bombs per case.

## Approach

Let $f(p) = \min_i \|p - b_i\|^2$ be the squared distance from $p$ to the closest bomb. Enumerating all $1001^3 = 1{,}003{,}003{,}001$ integer points per case is too slow. The solution is best-first branch and bound over inclusive integer boxes $B = (x_1, x_2, y_1, y_2, z_1, z_2)$.

For a box $B$ and one bomb $b = (b_x, b_y, b_z)$, the farthest any point of $B$ can be from that bomb maximizes each axis independently:

$$
\operatorname{maxdist}(b, B) = \max((b_x - x_1)^2, (b_x - x_2)^2) + \max((b_y - y_1)^2, (b_y - y_2)^2) + \max((b_z - z_1)^2, (b_z - z_2)^2)
$$

The bound is $U(B) = \min_i \operatorname{maxdist}(b_i, B)$. For any $p \in B$ and any bomb $b_i$, $\|p - b_i\|^2 \le \operatorname{maxdist}(b_i, B)$, hence $f(p) \le U(B)$. If the best point found so far has value $\ge U(B)$, no point in $B$ can improve it and the box is discarded. The bound is monotone: if $B' \subseteq B$ then $U(B') \le U(B)$, so descendants of a pruned box are pruned too.

Search steps:

1. Seed $\text{best}$ with the 8 cube corners, which are real evaluated points.
2. Push the root cube into a max-heap keyed by $U$.
3. Pop the box with the largest $U$. If $U \le \text{best}$, drop it; later pops have smaller keys.
4. If the box is a singleton, its $U$ is its exact value, so update $\text{best}$.
5. Otherwise split along the longest axis at its integer midpoint $m$ into $[l, m]$ and $[m + 1, h]$. These children share no integer points. Compute $U$ for each and push those with $U > \text{best}$.
6. When the heap is empty, $\text{best}$ is the answer.

The reach function exits as soon as any bomb has $\operatorname{maxdist} \le \text{best}$, since that alone proves $U \le \text{best}$. This avoids scanning all $N$ bombs for most pruned boxes. Coordinates are stored in flat lists and squared with multiplication rather than exponentiation.

The $T = 50$ cases are independent, so they are solved in a $12$-process pool. Cases are sorted by bomb count, largest first, so the expensive cases start together and the tail is short.

## Complexity

Computing $U$ costs $O(N)$ worst case per box, less with the early exit; evaluating a singleton costs $O(N)$. The number of visited boxes is data dependent, and memory is just the heap frontier. Branch and bound has an exponential theoretical worst case, but the bound tightens quickly as boxes shrink and these limits are comfortable.

## Time

~4.663 seconds.

Solved: 22 November 2026.

## Lessons

- The bound must be $\min_i \operatorname{maxdist}(b_i, B)$, not $\max_c \min_i \|c - b_i\|^2$. Swapping them prunes the optimum.
- Seed $\text{best}$ with actually evaluated points. Once $U$ is a true upper bound, starting $\text{best}$ at $U$ (or $U - 1$) claims an unachievable champion and prunes everything.
- The 8 cube corners give a strong initial incumbent for free; the exact answer is unchanged whether they are used or not.
- Best-first beats depth-first here by about $4\times$ ($14.6\text{s}$ vs $58.9\text{s}$ single process), because raising $\text{best}$ early is what prunes the search.
- Replacing exponentiation with multiplication and tuple indexing with flat lists was the largest single-process win ($23\text{s} \to 14.6\text{s}$), bigger than switching from an $8$-way split to a $2$-way split.
- Threads cannot speed up pure Python integer loops under the GIL. Process-level parallelism across cases took $14.6\text{s}$ to about $3\text{--}4\text{s}$.