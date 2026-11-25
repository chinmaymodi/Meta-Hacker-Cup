import time
start = time.time()

from collections import Counter

file = "second_hands_input.txt"

output = []

def solve(parts_count, display_limit, parts_list):
    if parts_count > 2 * display_limit:
        return "NO"
    parts_counter = Counter(parts_list)
    if any(d > 2 for _, d in parts_counter.items()):
        return "NO"
    return "YES"


with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        n, k = list(map(int, f.readline().split()))
        s_arr = list(map(int, f.readline().split()))
        output.append(solve(n, k, s_arr))

outputfile = "second_hands_output.txt"
with open(outputfile, 'w') as f:
    for ctr, val in enumerate(output, start=1):
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
