import time
start = time.time()

file = "ethan_finds_the_shortest_path_input.txt"

ans = []

'''
ok so the logic is, Ethan picks the shortest path at every turn
this means, the way we confuse his algorithm. is have 1 -> N cost k
and have 1 -> 2 cost k-1, so 2 is picked as next instead of N
and then, for the chain 1 -> 2 -> 3 -> 4 ... -> N-1 -> N
we assign the cost k-1, k-2, ... 1
Note that the edge that costs 1, must end on N
So the path that Ethan's algorithm picks, is costing min of
k-1 + k-2 + k-3 + ... + 1 {if k <= N}
or
k-1 + k-2 + k-3 + ... k-(N-1) {if k > N}
as opposed to the real shortest cost, k
'''

with open(file, 'r') as f:
    t = int(f.readline())

    for tc in range(1, t + 1):
        n, k = map(int, f.readline().split())

        # edge graph creation
        edges = []

        if n == 2:
            edges.append((1, 2, 1))
            val = 0

        elif k <= 3:
            # Force Ethan directly to N.
            edges.append((1, n, 1))
            val = 0

        else:
            val = (
                      (k * (k - 1) // 2)
                      if k <= n
                      else ((n - 1) * (2 * k - n) // 2)
                  ) - k

            edges.append((1, n, k))

            if k <= n:
                for j in range(1, k - 1):
                    edges.append((j, j + 1, k - j))

                edges.append((k - 1, n, 1))

            else:
                for j in range(1, n):
                    edges.append((j, j + 1, k - j))

        ans.append(str(val))
        ans[-1] += '\n'+str(len(edges))

        for u, v, w in edges:
            ans[-1] += '\n' + f"{u} {v} {w}"

outputfile = "ethan_finds_the_shortest_path_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')