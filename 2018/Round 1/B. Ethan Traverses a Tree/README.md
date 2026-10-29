[Meta-Hacker-Cup](../../../) / [2018](../../) / [Round 1](../) / B. Ethan Traverses a Tree

# B. Ethan Traverses a Tree

Given a binary tree (N nodes, rooted at 1, each node has left/right children and a label Li), Ethan's buggy `pre-order` algorithm actually produces the post-order label sequence. Assign labels 1..K to nodes such that Ethan's post-order output equals the true pre-order output. Every integer 1..K must appear at least once.

## Approach

Compute the pre-order sequence `P[1..N]` and post-order sequence `Q[1..N]` (node indices). For each position `i`, `P[i]` and `Q[i]` must share the same label. Union these pairs with DSU. Each DSU set must be monochromatic (one label). Different sets may share labels freely. If `S` = number of DSU sets, any label count from 1 to `S` is achievable. Possible iff `K <= S`.

## Complexity

O(N) time per test case - O(N) to build tree/traversals, O(N) for DSU unions and finds (DSU is effectively constant-time per operation). Optimal since all N nodes and N-1 edges must be read.

## Time

~0.547 seconds.

Solved: 29 October 2026.

## Lessons

- Pre-order and post-order sequences force label equality at matching positions: `pre[i]` and `post[i]` must share a label.
- DSU groups nodes that must share a label; each set is monochromatic.
- Different sets may share labels, so any label count 1..S is achievable.
- `K > S` -> Impossible. `K <= S` -> assign labels 1..K to K distinct sets, rest get label K.
- Replacing the tuple-based post-order stack with a two-stack approach dropped runtime from ~0.677s to ~0.547 seconds.
- Still sub-1 second, still happy.
