[Meta-Hacker-Cup](../../../) / [2017](../../) / [Qualification Round](../) / C. Fighting the Zombie

# C. Fighting the Zombie

A wizard must kill a zombie with a single spell. Each spell is written in dice notation: XdY means roll a Y-sided die X times and sum the results, and an optional XdY+Z or XdY-Z applies a flat modifier Z after the sum. Allowed die sizes are 4, 6, 8, 10, 12 and 20, with at most 20 dice per spell and a modifier up to 10,000. For each zombie the input gives its health H and the S prepared spells, and the answer is the largest probability that one cast deals at least H damage.

## Approach

Every spell reduces to three numbers: dice count X, die size Y, and modifier Z. The damage comes from the sum of X dice of Y sides, so the reachable totals only span 0 to X*Y, at most 20*20 = 400.

First build the exact frequency distribution for each of the 120 combinations of X in 1..20 and Y in {4, 6, 8, 10, 12, 20}. One die is uniform. For more dice, convolve the distribution of X-1 dice with the single-die distribution: every previous total is shifted by each face value and the counts accumulate. A dictionary caches each distribution, so no combination is ever rebuilt.

Second, convert every distribution into a suffix table, where entry i holds the number of outcomes whose total is at least i. This is one reverse pass per distribution.

Third, evaluate each spell. Reaching H total damage means the dice sum must reach H - Z, so the count of killing outcomes is the suffix entry at H - Z and the probability is that count divided by Y^X. Two guards run before the lookup: if the minimum roll plus modifier already reaches H the probability is 1, and if H - Z exceeds the maximum sum X*Y it is 0. The best probability over the S spells is printed to six decimals.

## Complexity

O(120 * 400) fixed precomputation for the distributions and suffix tables, then O(S) per zombie for the spell evaluation, so O(T*S) overall after startup.

## Time

~0.055 seconds.

Solved: 3 November 2026.

## Lessons

- 120 dice combinations cover the entire input space, so precomputing all of them once removes every repeated roll from the per-spell loop.
- Convolution extends a dice distribution: shift the previous distribution by each face value and add the counts.
- Suffix sums turn a threshold count into a single array lookup, replacing a scan over up to 400 entries with constant work.
- Health can reach 10,000 while damage never exceeds 400, so the minimum-roll and maximum-sum guards settle many cases before the table is touched.
- The suffix table took the runtime from about 0.50 seconds to about 0.05 seconds, a tenfold gain from moving work out of the inner loop into startup.
- With the tables in place, parsing and string handling dominate what is left.
