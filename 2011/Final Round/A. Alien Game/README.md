[Meta-Hacker-Cup](../../../) / [2011](../../) / [Final Round](../) / A. Alien Game

# A. Alien Game

Two players alternate moving apples in a line of $N$ buckets. Moving an internal positive bucket $a_i = y > 0$ does $(x, y, z) \mapsto (x+y, -y, z+y)$. The player with no legal move loses. Bucket $P$ is unknown with $|a_P| \le F$, and Popo moves first; count how many values of $a_P \in [-F, F]$ make Popo win under optimal play.

## Approach

Let $s_0 = 0$ and $s_k = \sum_{i=1}^{k} a_i$, i.e. prefix sums. Moving bucket $i$ turns $(s_{i-1}, s_i)$ from $(A+x, A+x+y)$ into $(A+x+y, A+x)$, so it swaps the two adjacent prefix sums while leaving every other $s_k$ unchanged. The move is legal exactly when $a_i = s_i - s_{i-1} > 0$, i.e. when that adjacent pair is increasing.

The endpoints $s_0$ and $s_N$ are not legal moves, so the game is played on $s_1, \ldots, s_{N-1}$. Define

$$
A = \#\{(p, q) : 1 \le p < q \le N-1,\; s_p < s_q\}.
$$

Swapping an adjacent increasing pair removes that pair from $A$ and leaves the relation of every other element with that pair unchanged, so each legal move reduces $A$ by 1. The terminal state is $s_1 \ge \cdots \ge s_{N-1}$, i.e. $A = 0$, so every line of play lasts exactly $A$ moves and there is no draw. Popo wins iff $A$ is odd.

Now split by the unknown bucket $P$. With $a_P = 0$ write base prefix sums $r_k$. Then

$$
L = [s_1, \ldots, s_{P-1}], \qquad R(v) = [r_P + v, \ldots, r_{N-1} + v].
$$

Pairs inside $L$ are fixed. Pairs inside $R(v)$ are fixed because $r_p + v < r_q + v \iff r_p < r_q$. Let $K = (A_1 + A_2) \bmod 2$. Only cross pairs change:

$$
s_p < r_q + v \iff v \ge d+1, \qquad d = s_p - r_q.
$$

Each cross pair contributes a flip at $v = d+1$. A threshold with even multiplicity flips parity twice and cancels; only odd-multiplicity $d$ values matter. With $C(v)$ the number of active cross pairs, $A(v) \equiv K + C(v) \pmod 2$, so the target is $C(v)$ odd when $K=0$ and even when $K=1$.

Sort the odd-multiplicity $d$ values. Values with $d < -F$ are active over the whole range and set the starting parity $p_0 = C(-F) \bmod 2$. Values with $d \ge F$ never activate. The rest split $[-F, F]$ into constant-parity blocks $[pos, d], [d+1, \ldots]$, so the answer is the total length of blocks whose parity matches the target.

The 50 cases are independent and solved in a 12-process pool.

## Complexity

Per case, $A_1, A_2$ are computed by merge sort in $O(N \log N)$ after counting equal pairs, cross-pair differences take $O(N^2)$, and sorting/scanning the $d$ values takes $O(N^2 \log N)$ worst case. Memory is $O(N^2)$ for the difference list.

## Time

~6.455 seconds.

Solved: 24 November 2026.

## Lessons

- Rewriting the move in prefix-sum space turns a strange state mutation into adjacent swaps with a simple legality condition. Understanding HOW the problem converts into a look at the prefix sum array, is what makes it possible in this timeframe.
- The ascending-pair count is an invariant: every legal move drops it by exactly 1, so the whole game collapses to parity.
    - This has a funny outcome/realization where the problem statement contains a lie. "The players at the Finals are so good that they only make optimal moves to maximize their chance of winning."    
      Every individual game $always$ has the same number of moves, no matter what order they are played in. So $how$ optimally a player plays, has no impact on whether they win or lose.
- The unknown bucket shifts one suffix of prefix sums by $v$, so cross-pair effects become threshold flips at $d+1$. Odd multiplicity is the only thing parity cares about.
- This approach takes about 27 seconds on a single process, versus a ~4.5 times reduction when using multiprocessing.