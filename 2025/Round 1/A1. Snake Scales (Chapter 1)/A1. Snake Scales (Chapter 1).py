import time

start = time.time()

file = "snake_scales_chapter_1_input.txt"
inp = []

with open(file, 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        platformLength = int(f.readline())
        if platformLength == 1:
            f.readline()
            inp.append(0)
            continue
        platforms = list(map(int, f.readline().split()))
        inp.append(max([abs(platforms[i] - platforms[i-1]) for i in range(1, platformLength)]))


outputfile = "snake_scales_chapter_1_output.txt"
with open(outputfile, 'w') as f:
    for ctr, val in enumerate(inp, 1):
        f.write("Case #%d: %s\n" % (ctr, val))
print(f'Total Time: {time.time() - start:.3f} seconds')