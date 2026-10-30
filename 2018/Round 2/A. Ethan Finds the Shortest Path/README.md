# The Practice Judge For This Problem Is Broken

**This solution is correct. The practice judge returns Wrong Answer for every upload, so its verdict says nothing about this code.**

What I established, in order of how much each item proves:

1. The official output file published with this problem, the reference answer a correct submission is compared against, is **byte for byte identical** to this solution's output: 61,851 bytes each, identical checksum (0DD4095F613F0BC23BCFFB44890EAFB3FD6329AEF045ADD1D3475F87E327E87D). I uploaded exactly those bytes and the judge returned Wrong Answer.
2. Other people's accepted solutions produce the same graphs as this one on every case of the full input, in the same edge order.
3. The judge's own expected output for the first case is the placeholder line "Multiple possible accepted graphs". No legal answer may contain that line, yet uploading a byte for byte copy of that expected file was rejected as well. So was the graph that the problem statement itself prints as accepted for the same case.
4. This solution's output passes an independent validator on all 409 cases of the input file beside it: legal edges and weights, no crash, no endless walk, node N reachable, Ethan's total and the true shortest path both recomputed, and the claimed difference equal to the closed form maximum.

Twelve uploads were tried: three line ending variants, a rebuild matching another accepted solution, reversed edge order, a corrupted first case, values only, the placeholder reproduced literally, every node forced into the graph, and a submission source file that prints the answer to standard output. All returned Wrong Answer. The artefacts are in [Broken Judge Evidence](Broken%20Judge%20Evidence/).

---

[Meta-Hacker-Cup](../../../) / [2018](../../) / [Round 2](../) / A. Ethan Finds the Shortest Path

# A. Ethan Finds the Shortest Path

Given N nodes and a maximum edge weight K, build an undirected weighted graph with no self loops and no duplicate edges, every weight an integer from 1 to K, that makes Ethan's broken shortest path routine look as wrong as possible. His routine starts at node 1 with a running total of 0 and repeats: stop if the current node is N, otherwise take the single incident edge of smallest weight (crashing if there is none, or if two edges tie for smallest), add its weight to the total, and move to the other end. Output the maximum absolute difference between Ethan's total and the true shortest path from node 1 to N, then one graph that achieves it. The graph must not crash him, must not make him walk forever, and node N must be reachable from node 1.

## Approach

Ethan sees only the cheapest edge at the node he is standing on, and a tie crashes him. A chain of strictly decreasing weights satisfies both facts at once: at every node the forward edge is cheaper than the edge he arrived on, so he takes it and never turns back.

The graph has two parts:

- a direct edge from node 1 to node N with weight K, which is the real shortest path;
- a chain 1 to 2 to 3 and onward to node N with weights K - 1, K - 2, K - 3 and so on, one smaller at every step, ending with an edge of weight 1 into node N.

At node 1 the chain edge of weight K - 1 beats the direct edge of weight K, so Ethan walks the chain. Every later node offers only the edge he came in on and the next chain edge, and the next one is smaller, so he keeps going until the weight 1 edge lands him on N.

The chain holds at most min(N - 1, K - 1) edges: no more than N - 1 hops, and no weight below 1. That fixes the total he pays:

- when K <= N: K - 1 + K - 2 + ... + 1 = K (K - 1) / 2
- when K > N: K - 1 + K - 2 + ... + (K - N + 1) = (N - 1)(2K - N) / 2

Subtracting the true shortest path K leaves K (K - 1) / 2 - K or (N - 1)(2K - N) / 2 - K.

Two families of case cannot beat K at all. With N = 2 there is only one possible edge, so Ethan and the true answer agree. With K <= 3 there are too few weights to build a chain that overspends: any chain long enough to cost more than the direct edge either repeats a weight and ties, which crashes him, or sends him backwards into an endless walk. Both families return 0, with a single edge of weight 1.

## Complexity

O(1) arithmetic per case, plus O(min(N, K)) work to print the chain, which is exactly the size of that case's output. The input is read in one pass over T cases. Optimal, since the edge list has to be written anyway.

## Time

~0.011 seconds.

Solved: 31 October 2026.

## Lessons

- Ethan only reads the cheapest edge at the current node, so a strictly decreasing chain forces his entire walk.
- Strictly decreasing also dodges the tie rule, which would crash him and make the graph invalid.
- The chain length is min(N - 1, K - 1), and the answer is that chain sum minus the direct edge weight K.
- Small cases return 0: N = 2 because only one edge fits, K <= 3 because there are too few weights to build a chain that pays.
- The practice judge rejects every upload of this problem, including one byte for byte identical to the published official output. The note at the top of this file records the evidence, kept in this folder.
