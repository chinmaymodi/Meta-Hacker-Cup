import time

start = time.time()

file = "wine_tasting_input.txt"

MOD = 1051962371
T = []
T.append([1] + ([0]*101))
for n in range(1, 101):
    T.append([])
    for k in range(101):
        temp = T[n-1][k]*(n-1-k) + T[n-1][k+1]*(k+1)
        if k >= 1:
            temp += T[n-1][k-1]
        T[-1].append(temp % MOD)
    T[-1].append(0)

ans = []
with open(file, 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        g, c = map(int, f.readline().split())
        ans.append(str(sum(T[g][c:]) % MOD))

outputfile = "wine_tasting_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')