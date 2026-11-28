import time
start = time.time()

KEY_SHIFT = 20


def solve(adjacency_list, query_iter):
    degree = [len(neighbours) for neighbours in adjacency_list]
    memo = {}
    get_memo = memo.get
    ans = []
    ans_append = ans.append

    for x, y in query_iter:
        if (degree[x], x) > (degree[y], y):
            x, y = y, x

        key = (x << KEY_SHIFT) | y
        val = get_memo(key)
        if val is None:
            total = 2 * adjacency_list[x].get(y, 0)

            get_y = adjacency_list[y].get
            for mid, cx in adjacency_list[x].items():
                cy = get_y(mid)
                if cy:
                    total += cx if cx < cy else cy

            memo[key] = total
            val = total

        ans_append(str(val))

    return ' '.join(ans)


def main():
    file = "second_flight_input.txt"
    outputfile = "second_flight_output.txt"

    with open(file, "rb") as f, open(outputfile, "w", newline="\n") as out:
        for case in range(1, int(f.readline()) + 1):
            n, m, q = map(int, f.readline().split())
            adj = [dict() for _ in range(n + 1)]
            for _ in range(m):
                a, b, capacity = map(int, f.readline().split())
                adj[a][b] = capacity
                adj[b][a] = capacity

            query_iter = (tuple(map(int, f.readline().split())) for _ in range(q))
            out.write(f"Case #{case}: {solve(adj, query_iter)}\n")

    print(f'Total Time: {time.time() - start:.3f} seconds')


if __name__ == "__main__":
    main()
