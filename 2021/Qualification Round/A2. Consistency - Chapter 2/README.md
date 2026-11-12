[Meta-Hacker-Cup](../../../) / [2021](../../) / [Qualification Round](../) / A2. Consistency - Chapter 2

# A2. Consistency - Chapter 2

Same goal as Chapter 1, except the legal moves are now given: K replacement types, each one letting Connie swap letter A_i for letter B_i anywhere in S. No ordered pair repeats, each type may be used any number of times, and one occurrence is replaced per second. Find the minimum seconds to make every letter in S identical, or -1 if it can never be done. A consistent string costs 0.

## Approach

Only 26 letters exist, so the rules form a directed graph on 26 nodes with unit-weight edges. Making the whole string equal to a target letter t costs, for every character, the shortest directed distance from its own letter to t, and the answer is the smallest such total that stays finite. A letter that cannot reach t makes that total infinite.

The solution keeps an adjacency list of the rules and runs one BFS per letter that appears in S, with a distance array so each node is enqueued once. Letters absent from S need no BFS, and each result is folded into a 26-slot cost array weighted by the letter's frequency. A target is marked unreachable the first time a present letter cannot reach it, and a letter's own slot contributes 0. The answer is the smallest total among targets not marked unreachable, or -1 if every target was.

## Complexity

O(d * (26 + K) + 26 * d) per case, where d <= 26 is the number of distinct letters in S, with O(26) space per BFS. The rules only cost the time to read them.

## Time

~0.014 seconds.

Solved: 13 November 2026.
