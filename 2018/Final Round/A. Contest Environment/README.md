[Meta-Hacker-Cup](../../../) / [2018](../../) / [Final Round](../) / A. Contest Environment

# A. Contest Environment

Alex (A) sits at the front-left desk, Borys (B) at the front-right desk of a 2xN classroom. They want to swap seats. Cooperative finalists (*) can move; uncooperative finalists (#) cannot. Empty desks (.) are free. Movement is allowed between adjacent desks in the same row or same column, except no sideways movement along the front row.

## Approach

- If either row contains `#` in the back row, output `Impossible` - the back row is the only highway between columns, and a `#` blocks it.
- Otherwise, count empty cells (`.`) in both rows and find the longest consecutive run of `#` in the front row.
- For any consecutive block of uncooperative finalists (`#`) in the front row of size `g`, you need `3 + g` empty chairs anywhere to let Alex and Borys swap through the back row.
- If `empty_count >= max_block_size + 3`, output `Possible`; otherwise `Impossible`.

## Example

Row 1: `A # .`  
Row 2: `. . .`

Blocking group in row 1: `#` at column 1 -> size 1.  
Empty cells: 3 in row 2 + 1 in row 1 (column 2) = 4 total.  
Need `3 + 1 = 4` empty chairs -> **Possible**.

## Complexity

O(N) time per test case - single pass over both rows.

## Time

~0.014 seconds.

Solved: 30 October 2026.

## Lessons

- Front row sideways movement is blocked, so both Alex and Borys must route through the back row.
- Uncooperative finalists (`#`) in the back row block the entire highway -> `Impossible`.
- Front row `#` blocks require `3 + block_size` empty chairs to maneuver around.
- Cooperative finalists (*) are treated as not being there, because they don't affect either count.
