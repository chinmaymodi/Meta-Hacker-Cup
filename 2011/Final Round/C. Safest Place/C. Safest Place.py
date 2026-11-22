import time

start = time.time()

from heapq import heappush, heappop
from multiprocessing import Pool

file = "safest_place_input.txt"
outputfile = "safest_place_output.txt"

def solve(bombs_array):
    n = len(bombs_array)
    xs = [b[0] for b in bombs_array]
    ys = [b[1] for b in bombs_array]
    zs = [b[2] for b in bombs_array]

    # calculate reach of a given box
    def get_reach(x_min, x_max, y_min, y_max, z_min, z_max, current_answer):
        max_reach = 1 << 60
        for i in range(n):
            bx = xs[i]
            by = ys[i]
            bz = zs[i]
            dx = bx - x_min
            t = x_max - bx
            if t > dx:
                dx = t
            dx *= dx
            dy = by - y_min
            t = y_max - by
            if t > dy:
                dy = t
            dy *= dy
            dz = bz - z_min
            t = z_max - bz
            if t > dz:
                dz = t
            dz *= dz
            d = dx + dy + dz
            if d <= current_answer:
                return d
            if d < max_reach:
                max_reach = d
        return max_reach

    def split2(x_min, x_max, y_min, y_max, z_min, z_max):
        sx = x_max - x_min
        sy = y_max - y_min
        sz = z_max - z_min
        if sx >= sy and sx >= sz:
            m = (x_min + x_max) >> 1
            return ((x_min, m, y_min, y_max, z_min, z_max),
                    (m + 1, x_max, y_min, y_max, z_min, z_max))
        if sy >= sz:
            m = (y_min + y_max) >> 1
            return ((x_min, x_max, y_min, m, z_min, z_max),
                    (x_min, x_max, m + 1, y_max, z_min, z_max))
        m = (z_min + z_max) >> 1
        return ((x_min, x_max, y_min, y_max, z_min, m),
                (x_min, x_max, y_min, y_max, m + 1, z_max))

    ans = -1
    for cx in (0, 1000):
        for cy in (0, 1000):
            for cz in (0, 1000):
                v = get_reach(cx, cx, cy, cy, cz, cz, ans)
                if v > ans:
                    ans = v
    temp_best = get_reach(0, 1000, 0, 1000, 0, 1000, ans)
    if temp_best <= ans:
        return str(ans)
    heap = [(-temp_best, 0, 1000, 0, 1000, 0, 1000)]
    while heap:
        neg_best, x1, x2, y1, y2, z1, z2 = heappop(heap)
        current_best = -neg_best
        if current_best <= ans:
            continue
        if x1 == x2 and y1 == y2 and z1 == z2:
            ans = current_best
            continue
        for child in split2(x1, x2, y1, y2, z1, z2):
            child_dist = get_reach(*child, ans)
            if child_dist > ans:
                heappush(heap, (-child_dist, *child))

    return str(ans)


if __name__ == "__main__":
    with open(file, 'r') as f:
        n = int(f.readline())
        cases = []
        for _ in range(n):
            bomb_count = int(f.readline())
            bombs = [list(map(int, f.readline().split())) for _ in range(bomb_count)]
            cases.append(bombs)

    order = sorted(range(n), key=lambda i: len(cases[i]), reverse=True)
    ordered_cases = [cases[i] for i in order]

    with Pool(12) as pool:
        results = pool.map(solve, ordered_cases, chunksize=1)

    output_array = [None] * n
    for idx, val in zip(order, results):
        output_array[idx] = val

    with open(outputfile, 'w') as f:
        ctr = 1
        for val in output_array:
            f.write("Case #" + str(ctr) + ": " + val + "\n")
            ctr += 1
    print(f'Total Time: {time.time() - start:.3f} seconds')
