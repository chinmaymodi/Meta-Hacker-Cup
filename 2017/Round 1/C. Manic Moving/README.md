[Meta-Hacker-Cup](../../../) / [2017](../../) / [Round 1](../) / C. Manic Moving

# C. Manic Moving

Wilson drives a truck that carries at most two families' sets of belongings at once. There are N towns joined by M roads, each road costing some litres of gas either way. K families move in order: family i from S[i] to a different town D[i], loaded before family j for i < j and delivered before family j. Wilson starts at town 1, pays for his own gas, and must finish every family or report that the schedule is impossible. Minimize the total gas.

## Approach

All-pairs shortest paths first, one Floyd-Warshall pass over the towns, since every leg of every candidate route is a shortest path between two towns.

Then a forward dynamic programming pass over the number of families fully handled, four states per count: zero loads held standing at the previous family's destination (or the headquarters before the first pickup), one load held standing at that same destination, one load held standing at the next family's start, two loads held standing at the second family's start. From the first state the only move is travel to the next start and load. From either one-load state the truck delivers the held load or travels on and loads the following family. From the two-load state the truck delivers the older load, since loads and deliveries both happen strictly in family order. Each transition advances the handled count by at most one, so one sweep over the counts settles every state. The answer is the zero-load state with all families handled, or -1 if it never became reachable.

## Complexity

O(N^3) per case for the all-pairs pass, then O(K) for the four-state sweep with O(1) transitions from each state. Space is O(N^2) for the distance table and O(K) for the states.

## Time

~6.563 seconds.

Solved: 5 November 2026.

## Lessons

- This solution caused a lot of problems with off by 1 issues and similar, because I chose to index towns from 0 rather than 1 as the constraints stated.
- The family index was one family too far in every transition past the first state, which filled the table with plausible numbers and got four of the five sample cases wrong. Naming exactly the family each transition touches fixed it.
- Both transitions out of the one-load-at-a-destination state started from the wrong town, and one of them had its destination on both ends, so that delivery leg cost zero. Using the town the truck was actually standing on, the previous family's destination, fixed both.
- The zero-length leg survived the first round of testing because case 1 ends with two families whose destinations are the same town, where the broken leg costs what the real leg costs. The other cases exposed it as soon as the index was fixed.
- The guards had been written against the wrong family index, which locked out the last delivery and the last pickup. After the index fix they followed from the largest family index each transition reads: nothing for writing into the next row, i < K-1 for family i+1, i < K-2 for family i+2.
- The cell for a load held at a destination was only ever written from the previous row's two-load state, so the cell for zero handled families stayed unreachable and the missing zero guard on the two transitions out of it never mattered. It would matter if that cell ever filled, since family_ends[-1] reads the last family silently.
- The break added once the sweep was correct was safe: no transition moves backward, so an unreachable row leaves every later row unreachable and the -1 branch still fires. All five sample cases and the large input stayed correct with it in place.
- Five timed runs averaged about 20 seconds, and the all-pairs pass is where it went: T*N^3 inner steps, about one hundred million at the input limits.\n- The speedup came from five changes, all inside the algorithm: the Floyd-Warshall and DP loops moved into functions so hot names are local instead of global (roughly 4x per element-step), the six per-family leg distances precomputed into flat lists before the sweep, four flat DP arrays instead of nested dp[row][state], inline comparisons replacing min() calls, and the same early break on an unreachable row. Time fell from ~20.069 seconds to ~6.563 seconds.
- I tried Dijkstra's from only the points of interest ({0} union starts union dests) instead of Floyd-Warshall over all towns; it ran slower (about 6.48s vs 6.29s on this input) because for the big cases nearly every town is a point of interest, so you're running ~100 heap-based Dijkstras on a 100-node graph, and the heap push/pop overhead in Python cancels the smaller operation count.
