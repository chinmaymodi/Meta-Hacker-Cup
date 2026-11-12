[Meta-Hacker-Cup](../../../) / [2021](../../) / [Qualification Round](../) / A1. Consistency - Chapter 1

# A1. Consistency - Chapter 1

Connie has a string S of uppercase letters and wants every letter in it to be the same. Each second she may pick one letter and replace it with a different one, but a vowel may only become a consonant and a consonant may only become a vowel. Repeated letters are replaced one occurrence per second. Find the minimum number of seconds, which is 0 if S is already consistent.

## Approach

The cost of turning one letter into a candidate target letter depends only on how the two relate:

- same letter: 0 seconds, nothing to do
- opposite class, vowel to consonant or consonant to vowel: 1 second, because that replacement is legal on its own
- same class but a different letter: 2 seconds, leaving through any letter of the other class and coming back, for example A to E via B

Both classes are non-empty, so the two-step route always exists and no case is impossible. Only 26 targets need considering, and that is the whole search space.

So score all 26 target letters at once. Keep a 26-slot array of running costs, and for each character of S add 1 to every slot holding a letter of the opposite class and 2 to every slot holding a different letter of the same class, skipping the character's own slot. The answer is the smallest total.

## Complexity

O(26 * |S|) per case, which is O(|S|) with a constant factor of 26, and O(1) extra space. The sum of |S| across all cases is at most 4500, so the worst allowed input is about 117000 additions.

## Time

~0.010 seconds.

Solved: 13 November 2026.