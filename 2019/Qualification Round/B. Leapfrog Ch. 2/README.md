[Meta-Hacker-Cup](../../../) / [2019](../../) / [Qualification Round](../) / B. Leapfrog Ch. 2

# B. Leapfrog Ch. 2

The same pond as Ch. 1 with two changes: the Alpha may leap over Beta Frogs to either its left or its right, and the Beta Frogs may hop into any adjacent empty pad. The Alpha starts on pad 1 and must reach pad N. Decide whether that is possible.

## Approach

Still need at least one empty pad (`dot_count > 0`), because every leap must land on an empty pad.

With two or more Beta Frogs (`b_count >= 2`), it is always possible: two Beta Frogs can shuffle so that at least one Beta Frog is always immediately to the Alpha's right with an empty pad beyond it, letting the Alpha inch toward the rightmost pad. For example: `ABB..` → `AB.B.` → `.BAB.` → `.B.BA` → `..BBA` → `.ABB.` — the Alpha advances one position while two Beta Frogs remain to its right, ready to repeat.

With exactly one Beta Frog (`b_count == 1`), the Alpha cannot maintain a moving leapfrog chain. The only solvable case is exactly one dot too (`b_count == dot_count == 1`), where the Beta Frog first shuffles next to the Alpha (`A.B` → `AB.`), after which the Alpha leaps over the single Beta Frog onto the single empty pad at the end.

With zero Beta Frogs, no leap is ever legal, so it always fails.

So the condition is `dot_count > 0` and (`b_count >= 2` or `b_count == dot_count`).

## Complexity

O(N) per case to count the two characters, O(1) extra space.

## Time

~0.005 seconds.

Solved: 6 November 2026.
