import time

start = time.time()

from itertools import accumulate
from collections import defaultdict
from multiprocessing import Pool
from bisect import bisect_left

file = "alien_game_input.txt"

def _ascending_pairs(arr):
    if len(arr) < 2:
        return 0

    def merge_sort(a):
        n = len(a)
        if n < 2:
            return a, 0
        mid = n // 2
        left, inv_left = merge_sort(a[:mid])
        right, inv_right = merge_sort(a[mid:])
        merged = []
        i = j = 0
        inv = inv_left + inv_right
        while i < len(left) and j < len(right):
            if right[j] < left[i]:
                merged.append(right[j])
                inv += len(left) - i
                j += 1
            else:
                merged.append(left[i])
                i += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    merged, inversions = merge_sort(arr)
    total_pairs = len(arr) * (len(arr) - 1) // 2
    equal_pairs = 0
    i = 0
    while i < len(merged):
        j = i + 1
        while j < len(merged) and merged[j] == merged[i]:
            j += 1
        count = j - i
        equal_pairs += count * (count - 1) // 2
        i = j
    return total_pairs - inversions - equal_pairs


def solve_case(bad_index, apples):
    left = apples[:bad_index]
    f = abs(apples[bad_index])
    left_prefix = list(accumulate(left))
    right = apples[bad_index+1:]
    right_prefix = list(accumulate(right, initial=(left_prefix[-1] if left_prefix else 0)))[:-1]

    parity = (_ascending_pairs(left_prefix) + _ascending_pairs(right_prefix)) & 1
    diffs = defaultdict(int)
    for i in range(len(left_prefix)):
        l = left_prefix[i]
        for j in range(len(right_prefix)):
            diffs[l - right_prefix[j]] += 1
    odd_d = sorted(d for d, c in diffs.items() if c & 1)
    target = 1 - parity
    ans = 0
    position = -f
    p = bisect_left(odd_d, -f) & 1
    for d in odd_d[bisect_left(odd_d, -f):bisect_left(odd_d, f)]:
        if p == target:
            ans += (d + 1) - position
        p ^= 1
        position = d + 1
    if p == target:
        ans += f - position + 1
    return str(ans)

def _run_case(indexed_case):
    index, case = indexed_case
    return index, solve_case(*case)


def main():
    cases = []
    with open(file, 'r') as f:
        t = int(f.readline())
        for _ in range(t):
            _, p = list(map(int, f.readline().split()))
            apples = list(map(int, f.readline().split()))
            cases.append((p - 1, apples))

    results = [None] * len(cases)
    with Pool(min(12, len(cases))) as pool:
        for index, val in pool.imap_unordered(_run_case, enumerate(cases)):
            results[index] = val

    outputfile = "alien_game_output.txt"

    with open(outputfile, 'w') as f:
        ctr = 1
        for val in results:
            f.write("Case #" + str(ctr) + ": " + val + "\n")
            ctr += 1

    print(f'Total Time: {time.time() - start:.3f} seconds')

if __name__ == "__main__":
    main()
