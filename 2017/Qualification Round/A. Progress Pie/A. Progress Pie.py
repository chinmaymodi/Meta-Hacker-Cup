import time
start = time.time()

import math
pi = math.pi

file = "progress_pie_input.txt"

def covered(t, x, y):

    px = x - 50
    py = y - 50

    a = 2.0 * pi * t / 100.0

    hx = math.sin(a)
    hy = math.cos(a)

    # cross(start, point)
    c1 = -px

    # cross(hand, point)
    c2 = hx*py - hy*px

    if t <= 50:
        return c1 <= 0 <= c2
    else:
        return not (c1 > 0 > c2)

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        p, x, y = map(int, f.readline().split())
        ans.append("black" if (x-50)**2 + (y-50)**2 <= 2500 and covered(p, x, y) else "white")


outputfile = "progress_pie_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
