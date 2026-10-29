import time
start = time.time()

file = "contest_environment_input.txt"

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        row1 = f.readline().strip()
        row2 = f.readline().strip()
        if '#' in row2:
            ans.append("Impossible")
            continue
        empty_count = row1.count('.') + row2.count('.')
        block_count = max(len(i) for i in row1.replace('A', '.').replace('B', '.').replace('*', '.').split('.'))

        ans.append("Possible" if empty_count >= block_count + 3 else "Impossible")


outputfile = "contest_environment_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
