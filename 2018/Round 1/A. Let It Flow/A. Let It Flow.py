import time
start = time.time()

file = "let_it_flow_input.txt"

ans = []
MOD = 10**9 + 7

with (open(file, 'r') as f):
    t = int(f.readline())
    for i in range(t):
        n = int(f.readline())
        if n % 2 == 1:
            ans.append("0")
            [f.readline() for _ in range(3)]
            continue
        pipes = []
        for _ in range(3):
            pipes.append(f.readline().strip())
        if pipes[0][0] == '#' or pipes[-1][-1] == '#':
            ans.append("0")
            continue
        a, b, c = 1, 0, 0 # where the water flows in, for column 0
        # Precompute passability for each column transition (j-1 -> j)
        can0 = [pipes[0][j - 1] != '#' and pipes[0][j] != '#' for j in range(1, n)]
        can1 = [pipes[1][j - 1] != '#' and pipes[1][j] != '#' for j in range(1, n)]
        can2 = [pipes[2][j - 1] != '#' and pipes[2][j] != '#' for j in range(1, n)]

        dp0, dp1, dp2 = 1, 0, 0
        for j in range(n - 1):
            if dp0 == 0 and dp1 == 0 and dp2 == 0:
                break
            n0 = dp1 if can0[j] else 0
            n1 = (dp0 + dp2)%MOD if can1[j] else 0
            n2 = dp1 if can2[j] else 0
            dp0, dp1, dp2 = n0, n1, n2
        ans.append(str(dp1))



outputfile = "let_it_flow_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
