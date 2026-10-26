import os
import time
from concurrent.futures import ProcessPoolExecutor


def solve_case(case):
    l, n, m, d, wi = case
    lo, hi = 0, l * min(wi)
    while lo < hi:
        mid = (lo + hi) // 2
        if sum(mid // w for w in wi) >= l:
            hi = mid
        else:
            lo = mid + 1
    wash_last = lo
    if m >= l:
        return wash_last + d
    wash = []
    for w in wi:
        k = wash_last // w
        if k:
            wash.extend(range(w, k * w + 1, w))
    wash.sort()
    total = 0
    K = -(-l // m)
    for u in range(K):
        v = wash[l - 1 - u * m] + (u + 1) * d
        if v > total:
            total = v
    return total


if __name__ == '__main__':
    start = time.time()
    cases = []
    with open('laundro_matt_input.txt', 'r') as f:
        t = int(f.readline())
        for _ in range(t):
            l, n, m, d = map(int, f.readline().split())
            wi = list(map(int, f.readline().split()))
            cases.append((l, n, m, d, wi))
    workers = min(12, os.cpu_count() or 1)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(solve_case, cases, chunksize=1))
    with open('laundro_matt_output.txt', 'w') as f:
        for ind, val in enumerate(results, 1):
            f.write("Case #" + str(ind) + ": " + str(val) + "\n")
    print(f'Total Time: {time.time() - start:.3f} seconds')
