import time
start = time.time()

file = "boomerang_constellations_input.txt"

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    print('Total test cases:', t)
    for i in range(t):
        n = int(f.readline())

        xs = [0] * n
        ys = [0] * n

        for j in range(n):
            xs[j], ys[j] = map(int, f.readline().split())

        stars = [{} for _ in range(n)]

        for j in range(n):
            xj = xs[j]
            yj = ys[j]
            dj = stars[j]

            for k in range(j + 1, n):
                dx = xj - xs[k]
                dy = yj - ys[k]
                dist = dx * dx + dy * dy

                dj[dist] = dj.get(dist, 0) + 1

                dk = stars[k]
                dk[dist] = dk.get(dist, 0) + 1

        a = 0

        for distances in stars:
            for d in distances.values():
                a += d * (d - 1) // 2

        ans.append(str(a))

outputfile = "boomerang_constellations_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
