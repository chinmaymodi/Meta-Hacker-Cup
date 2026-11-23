import time
from multiprocessing import Pool

start = time.time()

file = "party_time_input.txt"

output_array = []


def _run_case(indexed_case):
    index, case = indexed_case
    return index, solve_case(*case)

def solve_case(n, f, edges, food):
    import heapq

    base = 1000
    inf = 1 << 60

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    add = [0 if v < f else base * food[v] + 1 for v in range(n)]

    full = (1 << f) - 1
    dp = [[inf] * n for _ in range(full + 1)]

    if not hasattr(solve_case, "_splits"):
        solve_case._splits = {}
    if f not in solve_case._splits:
        cached = []
        for mask in range(full + 1):
            pairs = []
            if mask & (mask - 1):
                low = mask & -mask
                a = (mask - 1) & mask
                while a:
                    if a & low:
                        pairs.append((a, mask ^ a))
                    a = (a - 1) & mask
            cached.append(pairs)
        solve_case._splits[f] = cached
    splits = solve_case._splits[f]

    def relax(mask):
        row = dp[mask]
        heap = [(row[v], v) for v in range(n) if row[v] < inf]
        heapq.heapify(heap)
        while heap:
            dist, u = heapq.heappop(heap)
            if dist != row[u]:
                continue
            for v in adj[u]:
                nd = dist + add[v]
                if nd < row[v]:
                    row[v] = nd
                    heapq.heappush(heap, (nd, v))

    for i in range(f):
        mask = 1 << i
        dp[mask][i] = 0
        relax(mask)

    for mask in range(1, full + 1):
        if mask & (mask - 1) == 0:
            continue

        row = dp[mask]
        add_local = add
        inf_local = inf

        for a, b in splits[mask]:
            row_a = dp[a]
            row_b = dp[b]
            for v in range(n):
                left = row_a[v]
                if left == inf_local:
                    continue
                right = row_b[v]
                if right == inf_local:
                    continue
                candidate = left + right - add_local[v]
                if candidate < row[v]:
                    row[v] = candidate

        relax(mask)

    best = min(dp[full])
    final_key = best + base * sum(food[:f]) + f
    return str(final_key // base) + " " + str(final_key % base)


def main():
    cases = []
    with open(file, 'r') as f:
        n = int(f.readline())
        for _ in range(n):
            N, F, M = map(int, f.readline().split())
            edges = []
            for _ in range(M):
                u, v = map(int, f.readline().split())
                edges.append((u, v))
            food = list(map(int, f.readline().split()))
            cases.append((N, F, edges, food))

    results = [None] * len(cases)

    if len(cases) <= 1:
        for index, case in enumerate(cases):
            results[index] = solve_case(*case)
    else:
        with Pool(min(12, len(cases))) as pool:
            for index, val in pool.imap_unordered(_run_case, enumerate(cases)):
                results[index] = val

    output_array.extend(results)

    outputfile = "party_time_output.txt"

    with open(outputfile, 'w') as f:
        ctr = 1
        for val in output_array:
            f.write("Case #" + str(ctr) + ": " + val + "\n")
            ctr += 1

    print(f'Total Time: {time.time() - start:.3f} seconds')


if __name__ == "__main__":
    main()
