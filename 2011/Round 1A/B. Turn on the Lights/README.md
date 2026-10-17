[Meta-Hacker-Cup](../../../) / [2011](../../) / [Round 1A](../) / B. Turn on the Lights

# B. Turn on the Lights

A grid of lamps is given, where `X` marks a lamp that is on and `.` marks a lamp that is off. Pressing a lamp toggles its own state and the state of every lamp orthogonally adjacent to it. Find the minimum number of presses that turns every lamp on, or -1 if no sequence of presses can do it.

## Approach

Transpose the grid when needed so that there are fewer columns than rows, and read each row as a bitmask. The top row is the only real choice: once its presses are fixed the rest of the board is forced, because the only remaining press that can reach a lamp still off in the row above is the one directly below it. Chasing downward that way solves the board exactly when the last row comes out fully lit.

The last row is an affine function of the top-row guess g:

```
bottom(g) = start_bottom XOR columns[k]   (for each bit k set in g)
```

where `start_bottom` is the last row after chasing with an empty top row, and `columns[k]` is how much the last row changes when only lamp k of the top row is pressed. Both come from C+1 chases. Instead of trying all 2^C guesses, the system `bottom(g) = all_on` is solved directly with a linear basis, which gives every valid top row at once. The free columns of that solve are enumerated and each candidate is chased for its press count, and a case with no solution prints -1.

## Complexity

O(R * C) per test case, plus one chase per candidate top row.

## Time

~0.01 seconds.

Solved: 18 October 2026.

## Lessons

- The first version tried all 2^C top rows and chased the whole board for each one. It worked, but it took about 80 seconds. The downward pass is the usual [light chasing](https://en.wikipedia.org/wiki/Lights_Out_(game)) method, pressing the row below to clear the row above.
- The next version noticed that the last row is just the XOR of what each single-lamp top-row press does to it, so those C masks can be precomputed once and combined with XOR instead of chasing every guess. That dropped the runtime to about 3 seconds.
- The final version stops guessing. Reading the board as a system over XOR, it solves the system with a [linear basis](https://codeforces.com/blog/entry/68953) (Gaussian elimination where subtraction is XOR) and only chases the free variables that remain, which runs in about 0.01 seconds.
