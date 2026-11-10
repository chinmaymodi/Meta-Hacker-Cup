[Meta-Hacker-Cup](../../../) / [2020](../../) / [Round 2](../) / A. Ca-pasta-ty

# A. Ca-pasta-ty

Pascal's restaurant has N seating sections. Section i starts with S_i customers, and to stay within capacity rules it has to end up seating between X_i and X_i + Y_i customers, inclusive. He may repeatedly pick one customer and relocate them from their current section to any other section. Find the minimum number of relocations, or -1 if the counts can never all satisfy the rules.

Only the first K values of the S, X and Y series are given. The rest are produced by three independent linear recurrences.

## Approach

One pass over the sections, sorting each into one of three cases and keeping four running totals:

- below its range (S_i < X_i): it has to gain X_i - S_i customers, and it has room for at most X_i + Y_i - S_i
- above its range (S_i > X_i + Y_i): it has to lose S_i - X_i - Y_i customers, and it can spare at most S_i - X_i
- already inside its range: nothing is forced, but it has room for up to X_i + Y_i - S_i more, or can give away up to S_i - X_i

A relocation takes one customer from a section that has to shrink and puts them in a section that has to grow, so a single move helps both sides at once. That makes the answer the larger of the two forced totals. It is impossible when the customers that have to leave cannot fit into the room that exists, or when the customers that are needed cannot come from anywhere.

## Complexity

O(N) per day and constant extra space beyond the three generated series. The sum of N across all days is at most 10,000,000, so this one pass is the entire cost.

## Time

~3.830 seconds.

Solved: 11 November 2026.

## Lessons

- The first version never added to the "has room" and "can spare" totals in two of the three branches, so valid days were reported as impossible. The forced totals were right, the spare capacity totals were not.
- The three series come from independent recurrences, so all three can be advanced in one loop instead of three passes over the input.
- A `for` loop over `repeat(None, n - k)` is cheaper than `while k < n`, since there is no counter to compare and increment millions of times.
- The inner loop runs millions of times per day and touches a lot of variables, so simply reading and writing those variables was most of the runtime.
- Wrapping the whole solve in `main()` took it from ~12-14 seconds to ~3.830 seconds, about 3.3x, by changing nothing except where the code lives. Python handles variables faster inside a function than at file level.
