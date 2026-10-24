[Meta-Hacker-Cup](../../../) / [2015](../../) / [Qualification Round](../) / B. New Year's Resolution

# B. New Year's Resolution

Determine if it is possible to select a subset of foods that exactly match the required protein, carbohydrate, and fat content.

## Approach

This is a subset sum problem in three dimensions. With $N \approx 20$, the search space is $2^N \approx 10^6$, which is small enough for efficient exploration. The optimal approach is backtracking with pruning. It explores the decision tree and stops immediately if the remaining requirements drop below zero.

## Complexity

O(2^N) per test case, where N is the number of foods. Pruning makes this significantly faster than the worst case in practice.

## Time

~0.008 seconds.

Solved: 24 October 2026.

## Lessons

- **Case 1a: Inefficient bitmask.** Mistakenly did zip of entire array based on bitmask, to try and write less code. Ended up being extremely inefficient and took over 120 seconds.
- **Case 1b: Improved bitmask.** Turns out, the inefficiency is in the eye of the bi(tmask)holder. Even improving the code and not recreating a zipped list, only took the time down to about ~90 seconds. Massive improvement, still worthless.
- **Case 2: Backtracking.** The first attempt was incorrect because I forgot 'return a or b' in python fails for strings, because non-empty strings are True. So if a returns 'no', we simply return 'no' for the whole thing instead of checking the other path. Upon fixing and running it, much faster, ~0.008 seconds.
- **Case 3: Memoized DP.** Unless I drastically misunderstood, this is essentially backtracking with memoization. I implemented it, but as it turns out, the overhead of caching actually worsens the runtime as opposed to default backtracking. Takes ~0.017 seconds, which is still blazingly fast, but practically doubling the backtracking runtime.
