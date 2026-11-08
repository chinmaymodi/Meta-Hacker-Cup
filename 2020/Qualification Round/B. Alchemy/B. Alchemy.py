import time
start = time.time()

file = "alchemy_input.txt"

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        tot = int(f.readline())
        shard_string = f.readline().strip()
        a_count = shard_string.count('A')
        ans.append('Y' if abs(2*a_count - tot) == 1 else 'N')

outputfile = "alchemy_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
