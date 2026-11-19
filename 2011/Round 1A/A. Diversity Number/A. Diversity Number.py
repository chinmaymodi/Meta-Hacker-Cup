import time

start = time.time()

file = "diversity_number_input.txt"

output = []

def solve(test_arr):
    test_arr = [1] + [x+2 for x in test_arr] + [2]
    n = len(test_arr)
    MOD = 1000000007

    left = []
    for i in range(n):
        ai = test_arr[i]
        s = set()
        cs = []
        for k in range(i + 1, n):
            v = test_arr[k]
            if v >= ai and v not in s:
                s.add(v)
                cs.append(k)
        left.append(cs)
    right = []
    for j in range(n):
        aj = test_arr[j]
        s = set()
        cs = []
        for k in range(j - 1, -1, -1):
            v = test_arr[k]
            if v >= aj and v not in s:
                s.add(v)
                cs.append(k)
        right.append(cs)

    cur = [[0] * n for _ in range(n)]
    nxt = [[0] * n for _ in range(n)]
    stamp = [[0] * n for _ in range(n)]
    gen = 0
    cur[0][n - 1] = 1
    active = [(0, n - 1)]
    ans = 0
    for m in range(n + 1):
        if not active:
            break
        gen += 1
        touched = []
        for i, j in active:
            ways = cur[i][j]
            ai = test_arr[i]
            aj = test_arr[j]
            if ai <= aj:
                if ai > m and aj > m + 1:
                    ans += (aj - m - 1) * (ai - m) * ways
                if ai > m:
                    base = (ai - m) * ways
                    for k in left[i]:
                        if k >= j:
                            break
                        if stamp[k][j] != gen:
                            stamp[k][j] = gen
                            nxt[k][j] = base
                            touched.append((k, j))
                        else:
                            nxt[k][j] += base
            else:
                if aj > m and ai > m + 1:
                    ans += (ai - m - 1) * (aj - m) * ways
                if aj > m:
                    base = (aj - m) * ways
                    for k in right[j]:
                        if k <= i:
                            break
                        if stamp[i][k] != gen:
                            stamp[i][k] = gen
                            nxt[i][k] = base
                            touched.append((i, k))
                        else:
                            nxt[i][k] += base
        active = []
        for i, j in touched:
            v = nxt[i][j] % MOD
            nxt[i][j] = 0
            if v:
                cur[i][j] = v
                active.append((i, j))

    return str(ans % MOD)

with open(file, 'r') as f:
    for _ in range(int(f.readline())):
        f.readline()
        input_array = list(map(int, f.readline().split()))
        output.append(solve(input_array))


outputfile = "diversity_number_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
