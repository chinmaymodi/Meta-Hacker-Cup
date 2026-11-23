[Meta-Hacker-Cup](../../../) / [2011](../../) / [Final Round](../) / B. Party Time

# B. Party Time

Pick a connected set of people containing all $F$ friends, minimizing total food and, on a tie, the number of guests. There are $T = 50$ cases, at most $N = 250$ people, and $F \le 11$. Edges are free; only the people you invite cost food.

## Approach

The first $F$ people are friends. Any solution is a connected vertex set containing them all. If the induced set has a cycle, delete any edge on that cycle: connectivity and guest count are unchanged, so some optimum is a tree. The DP therefore computes cheapest connected vertex sets and never needs to enforce acyclicity.

Both objectives are folded into one integer:

$$
\text{key} = 1000 \cdot \text{food} + \text{guests}
$$

Since $N \le 250 < 1000$, the guest count fits in the last three digits and never carries into the food part. Comparing keys minimizes food first, then guests.

Friend food is deferred. Define the cost of entering a node:

$$
\operatorname{enter}(v) =
\begin{cases}
0 & v < F \\
1000 \cdot \text{food}[v] + 1 & v \ge F
\end{cases}
$$

Let $dp[S][v]$ be the cheapest packed key of a connected set containing exactly the friends in mask $S$ and containing node $v$. The table has at most $2^{11} \times 250$ cells.

**Singleton rows.** For each friend $i$, set $dp[1 \ll i][i] = 0$ and run Dijkstra with edge weight $\operatorname{enter}(v)$. Because entering friends is free, this correctly charges only the non-friend connectors on the paths.

**Merging.** Process masks in numeric order from 1 to $(1 \ll F) - 1$. Numeric order suffices because every proper submask of $S$ is strictly less than $S$. For each mask, enumerate each unordered split $S = A \cup B$ once using the low-bit trick:

```python
low = S & -S          # lowest friend bit in S
A = (S - 1) & S       # largest proper submask
while A:
    if A & low:       # keep only splits where A holds the lowest bit
        B = S ^ A     # set difference, since A is a submask
        ...
        A = (A - 1) & S
```

Requiring $A$ to contain the lowest bit discards the mirror-image splits. For each node $v$:

$$
dp[S][v] = \min\bigl(dp[S][v],\; dp[A][v] + dp[B][v] - \operatorname{enter}(v)\bigr)
$$

Both halves contain $v$, so $v$ was counted twice. If $v$ is a connector, subtracting $\operatorname{enter}(v)$ removes one copy of its food and one guest. If $v$ is a friend, $\operatorname{enter}(v) = 0$ and nothing is removed, because friend food is added once at the end.

After all splits for a mask, run Dijkstra again from every finite cell of that row, so a combined group can also grow to new connector nodes.

**Answer.** At the full mask:

$$
\text{best} = \min_v dp[(1 \ll F) - 1][v]
$$

Then add back the fixed friend portion and decode:

$$
\text{final} = \text{best} + 1000 \sum_{i < F} \text{food}[i] + F
$$

$$
\text{food} = \text{final} \mathbin{//} 1000, \qquad \text{guests} = \text{final} \bmod 1000
$$

The $T = 50$ cases are independent, so they are solved in a 12-process pool with `imap_unordered`, and results are written back in original case order.

## Complexity

The number of unordered splits summed over all masks is $\tfrac12(3^F - 2^{F+1} + 1)$, which is $O(3^F)$; each scans $N$ nodes, so the merge phase is $O(3^F \cdot N)$. For $F = 11$ and $N = 250$ that is $86{,}526$ splits and about 21.6 million inner iterations per case. Each mask also runs a Dijkstra, $O(M \log N)$ on sparse inputs and $O(N^2 \log N)$ worst case. Memory is $O(2^F \cdot N)$.

## Time

~55.046 seconds.

Solved: 23 November 2026.

## Lessons

- Packing the two objectives as $1000 \cdot \text{food} + \text{guests}$ makes the tie-break fall out of integer comparison. The base only needs to exceed $N$.
- Deferring friend costs makes every singleton start at 0 and removes friend bookkeeping from the merge. Add friends back once, at the end.
- The low-bit rule halves the split count by keeping only splits where $A$ contains the lowest friend bit. Numeric mask order is enough because every proper submask is smaller.