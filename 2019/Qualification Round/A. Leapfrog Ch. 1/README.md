[Meta-Hacker-Cup](../../../) / [2019](../../) / [Qualification Round](../) / A. Leapfrog Ch. 1

# A. Leapfrog Ch. 1

N lilypads sit in a row. The Alpha Frog starts on pad 1 and must reach pad N. The Alpha may leap only to its right, over one or more Beta Frogs, landing on the next unoccupied pad past them, and must clear at least one Beta Frog per leap. Any Beta Frog may hop one pad left or right into an empty spot. Decide whether the Alpha can reach the rightmost pad.

## Approach

Two conditions:

1. At least one empty pad must exist (`dot_count > 0`), because every leap needs an empty pad to land on, including the final landing on the rightmost pad.
2. There must be at least as many Beta Frogs as dots (`b_count >= dot_count`). Every dot the Alpha passes costs one or more Beta Frogs to leap over, and the Beta Frogs can shuffle left and right so that, with enough of them, they can always be arranged into a jumpable configuration right up to the last pad.

So the condition is `dot_count > 0` and `b_count >= dot_count`.

## Complexity

O(N) per case to count the two characters, O(1) extra space.

## Time

~0.005 seconds.

Solved: 6 November 2026.
