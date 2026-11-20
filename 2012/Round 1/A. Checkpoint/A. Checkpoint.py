import time
start = time.time()

file = "checkpoint_input.txt"

from math import comb

first_seen = {}

LIMIT = 10**7

for n in range(1, 4473):
    for k in range(0, n // 2 + 1):
        c = comb(n, k)
        if c > LIMIT:          # rest of the row only gets bigger
            break
        if c not in first_seen:
            first_seen[c] = n

def solve(n):
    fs = first_seen
    def divisors(n):
        out = []

        i = 1
        while i * i <= n:
            if n % i == 0:
                out.append(i)
            i += 1

        return out
    ans = 10**10
    for d in divisors(n):
        a = fs.get(d, d)
        b = fs.get(n // d, n // d)
        if a + b < ans:
            ans = a + b
    return ans


output = []
with open(file, 'r') as f:
    for _ in range(int(f.readline())):
        output.append(str(solve(int(f.readline()))))

outputfile = "checkpoint_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')