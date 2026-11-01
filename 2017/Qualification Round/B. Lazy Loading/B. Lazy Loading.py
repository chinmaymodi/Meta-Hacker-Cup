import time
start = time.time()

from math import ceil

file = "lazy_loading_input.txt"

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        n = int(f.readline())
        weights = [int(x) for _ in range(n) for x in f.readline().split()]
        weights.sort()
        r = len(weights) - 1
        l = 0
        val = 0
        while l <= r:
            current_weight = weights[r]
            needed_count = ceil(50/current_weight) - 1
            if l + needed_count <= r:
                l += needed_count
                val += 1
                r -= 1
            else:
                break
        ans.append(str(val))


outputfile = "lazy_loading_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
