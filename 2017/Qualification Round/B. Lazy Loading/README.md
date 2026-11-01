[Meta-Hacker-Cup](../../../) / [2017](../../) / [Qualification Round](../) / B. Lazy Loading

# B. Lazy Loading

Wilson wants to maximize the number of bag trips to move items, but Julie will berate him if any trip appears to have less than 50 pounds. When Julie sees a bag with k items where the top item weighs w, she assumes the bag weighs at least k*w. Wilson must pack all items so that each bag appears to weigh at least 50 pounds.

## Approach

Sort the item weights ascending. Wilson should maximize the number of bags by making each bag as small as possible while still satisfying Julie's constraint.

Key insight: If a bag has weight w on top and contains k items, Julie sees it as weighing k*w. To satisfy the minimum, k >= ceil(50/w). To minimize items per bag (maximize bag count), use exactly k = ceil(50/w) items.

Greedy strategy: Pick the heaviest remaining item as the top (w), then fill the bag with the lightest remaining items. This ensures:
1. Heavy items act as tops, requiring fewer items per bag (smaller ceil(50/w))
2. Light items fill bags, preserving heavier items to serve as tops later
3. If top item is w and we add ceil(50/w)-1 lighter items, the constraint k*w >= 50 is exactly satisfied

Two-pointer implementation: r points to the heaviest remaining item, l to the lightest. Pop r as top, calculate needed_count = ceil(50/w) - 1, if possible add needed_count items from l, increment bag count, repeat.

## Complexity

O(N log N) time per test case from sorting, O(N) for the greedy pairing.

## Time

~0.056 seconds.

Solved: 2 November 2026.

## Lessons

- Greedy pairing: always pair heaviest top with lightest fillers to minimize fillers per top.
- The constraint ceil(50/w) is tight - Wilson cannot do better than using exactly that many items per bag with a given top weight.
- Sorting enables the two-pointer greedy: after sorting ascending, indices l and r can scan from both ends.
- Each item is used exactly once: items at r serve as tops, items at l serve as fillers.
- Algorithm terminates when ceil(50/w) items cannot be formed from remaining items.