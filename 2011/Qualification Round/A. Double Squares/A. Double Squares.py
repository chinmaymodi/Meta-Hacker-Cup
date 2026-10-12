import time
start = time.time()
import math
from functools import cache

file = "double_squares_input.txt"
@cache
def calc(v):
    ans = 0
    max_a = math.isqrt(v)
    for aa in range(max_a + 1):
        b2 = v - aa * aa
        b = math.isqrt(b2)
        if aa > b:
            break
        if b * b == b2:
            ans += 1
    return ans

inp = []
with open(file, 'r') as f:
    f.readline()
    for line in f.readlines():
        val = int(line)
        inp.append(val)

outputfile = "double_squares_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in inp:
        f.write("Case #" + str(ctr) + ": " + str(calc(val)) + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')