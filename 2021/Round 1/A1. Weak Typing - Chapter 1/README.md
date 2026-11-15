[Meta-Hacker-Cup](../../../) / [2021](../../) / [Round 1](../) / A1. Weak Typing - Chapter 1

# A1. Weak Typing - Chapter 1

Timmy types each exercise with one hand while the other holds a popsicle. His left hand reaches F and X, his right hand reaches F and O. He may start on either hand, end on either hand, and switch whenever he needs to. Find the minimum number of hand switches required to type a string made of the letters F, O and X.

## Approach

F is the one letter both hands can reach, so it never forces a switch. Whatever hand typed the character before it can type the F, and that same hand is still in use afterwards. Ignoring every F therefore leaves the answer unchanged.

What is left is a string over O and X: O is right-only, X is left-only. So two consecutive characters of the stripped string cost 0 when they match and 1 when they differ, and no arrangement does better. The F's that sat between them are worth nothing, because each one is typed by the hand already in use.

The answer is the number of X and O pairs in the stripped string whose letters differ, which is the number of maximal blocks minus one, with an empty or single-block result giving 0.

## Complexity

O(N) time per exercise, one pass over the line with no nested work. Extra space is O(1) beyond the input line itself. The limits allow N up to 800,000 and a total of 4,000,000 characters across all exercises; the shipped input holds 116 exercises, more than the stated T <= 80 bound, totalling 2,453,224 characters with the longest at 800,000.

## Time

~0.19 seconds.

Solved: 15 November 2026.
