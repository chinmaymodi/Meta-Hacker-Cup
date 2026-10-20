[Meta-Hacker-Cup](../../../) / [2025](../../) / [Practice Round](../) / A. Warm Up

# A. Warm Up

N dishes each start at a temperature and need to reach a target temperature. One operation picks two dishes at different temperatures and warms the colder one to the temperature of the hotter one. Print a valid sequence of operations, or -1 if the targets cannot be reached.

## Approach

A dish can only be warmed, never cooled, so a case is impossible when some target is below its starting temperature. No operation creates a new temperature either, because the colder dish always takes a temperature another dish already has, so a case is also impossible when some target temperature never appears among the starting temperatures.

Otherwise, process target temperatures in ascending order. Bucket each dish that needs to move by its target temperature and keep one witness dish for each starting temperature. For a target `t`, the first dish that needs `t` is warmed by the witness at `t`, and every later dish that needs `t` is warmed by the dish moved immediately before it, which is now at `t`. The operations for one target therefore form a chain that starts at the witness.

Ascending order is what makes the chain safe: a dish at temperature `t` can only move when its own target, which is at least `t`, is processed, so it is still at `t` while target `t` is handled.

## Complexity

O(N) per test case.

## Time

~1.8 seconds.

Solved: 20 October 2026.

## Lessons

- The first version sorted the dishes by `(target, current)` and kept a set of dish indices for every temperature, moving an index from one set to another for each operation. It ran in 3+ seconds.
- Both are unnecessary. Bucketing the dishes by target temperature is a single counting-style pass instead of a comparison sort, and one witness per temperature is enough because every dish moved becomes the witness for the next one in the same chain. Together they brought the run down to under 2 seconds.
- Writing the output line by line was also measurable: about 0.5 seconds across the dataset, against about 0.08 seconds for one joined write per case.
