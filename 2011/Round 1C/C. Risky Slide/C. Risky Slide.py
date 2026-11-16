import time
start = time.time()

from bisect import bisect_right
from itertools import accumulate

file = "risky_slide_input.txt"

def solve(test_grid):
    ans = 0
    def get_best(lines):
        nonlocal ans
        for line in lines:
            for p in ([0, *accumulate(line)], [0, *accumulate(reversed(line))]):
                for i in range(1, len(p) - 1):
                    j = bisect_right(p, 2 * p[i]) - 1
                    if j - i > ans:
                        ans = j - i

    get_best(test_grid)
    get_best(zip(*test_grid))
    return str(ans)
output = []
with open(file, 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        rows = int(f.readline().split()[0])
        grid = [[int(ch) for ch in f.readline().strip()] for _ in range(rows)]
        output.append(solve(grid))

outputfile = "risky_slide_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')