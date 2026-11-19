[Meta-Hacker-Cup](../../../) / [2011](../../) / [Round 1A](../) / A. Diversity Number

# A. Diversity Number

Given a list of $N$ integers, sum the diversity of every mountain subsequence, modulo $10^9 + 7$. A subsequence is a mountain if it weakly increases to a peak and then weakly decreases. The diversity of a sequence is found by sorting it into $c_0 \le c_1 \le \dots$ and multiplying $(c_i - i)$ over every position $i$ (0-based); if any factor is non-positive the diversity is 0. Two subsequences that are identical as value sequences count only once. The empty subsequence contributes 1, the empty product.

## Approach

Pad the array to `a = [1] + [x + 2 for x in nums] + [2]`. The two sentinels are live ends with neutral factors ($1 - 0 = 1$ and $2 - 1 = 1$), and shifting every real value by $+2$ cancels the two extra frozen ranks. The sentinels then drop out of the arithmetic and the empty subsequence is counted.

Let `dp[m][i][j]` be the weighted count after freezing $m$ values, with the live ends at indices $i$ and $j$. Freezing always takes the smaller live end, so values freeze in ascending order and $m$ is the rank of the last frozen value. From each state:

- Grow: freeze `a[i]` when `a[i] <= a[j]`. The new left end is some $k$ with $i < k < j$ and $a[k] \ge a[i]$, taking only the first occurrence of each distinct value, and the count gains a factor $(a[i] - m)$. Freezing the right end is symmetric with factor $(a[j] - m)$.
- Close: when both ends are the largest remaining values ($a[i] > m$ and $a[j] > m + 1$), add $(a[j] - m - 1)(a[i] - m)$ to the answer.

Only two rolling layers are kept, `cur` and `nxt`, as 2D lists instead of all $n + 1$ layers, with direct `nxt[k][j]` indexing. The loop visits only the nonzero states in an `active` list, not every $(i, j)$ cell. Distinct-value candidate positions are precomputed once per index into `left` / `right`, so the inner loop has no `set` allocation or value comparison. A generation `stamp` marks cells written this round, so `nxt` needs no clearing and `touched` rebuilds `active`.

## Complexity

$n = N + 2 \le 102$. The DP has $O(n^3)$ states $(m, i, j)$, each expanding over up to $O(n)$ distinct-value candidates. Memory is $O(n^2)$ for the two rolling layers plus the precomputed candidate lists. On the 60-case judge input (sum $M = 4114$) the sparse implementation touches about 1.7M nonzero states and 18.8M transitions.

## Time

~4.094 seconds.

Solved: 19 November 2026.

## Lessons

- The dense version would scan every $(i, j)$ cell on every layer and hit `continue` on most of them. Keeping a list of the nonzero states skips that work.
- Building the distinct-value candidate lists once per index removes the `set` allocation and membership check from the inner loop. Direct 2D indexing removes a multiply and add from the innermost statement.
- A generation stamp is a lazy clear. One integer increment empties the `nxt` grid logically, replacing an $n^2$ clear pass per round, and doubles as the "written this round" flag so each coordinate lands in `touched` once.
- Values entering `cur` are already reduced mod $MOD$ at write time, so reducing again on read is wasted.
- This forward build iterative version is about twice as fast as the recursive version, which was my initial idea.