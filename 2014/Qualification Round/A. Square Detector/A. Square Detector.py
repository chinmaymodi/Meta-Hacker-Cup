import time
start = time.time()

file = "square_detector_input.txt"

inp = []
with open(file, 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        num_lines = int(f.readline())
        minx = miny = num_lines
        maxx = maxy = 0
        count = 0
        for i in range(num_lines):
            line = f.readline()
            for j in range(num_lines):
                if line[j] == '#':
                    minx = min(minx, i)
                    miny = min(miny, j)
                    maxx = max(maxx, i)
                    maxy = max(maxy, j)
                    count += 1
        # print(minx, maxx, miny, maxy, count)
        if maxx - minx == maxy - miny and count == (maxx - minx + 1)**2:
            inp.append("YES")
        else:
            inp.append("NO")

outputfile = "square_detector_output.txt"
with open(outputfile, 'w') as f:
    for ind, val in enumerate(inp, 1):
        f.write("Case #" + str(ind) + ": " + str(val) + "\n")
print(f'Total Time: {time.time() - start:.3f} seconds')