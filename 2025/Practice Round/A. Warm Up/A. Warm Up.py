import time

start = time.time()

file = "warm_up_input.txt"
inp = []

with open(file, 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        count = int(f.readline())
        currentTemps = list(map(int, f.readline().split()))
        targetTemps = list(map(int, f.readline().split()))

        first_at = [-1] * (count + 1)
        bad = False
        for i in range(count):
            a = currentTemps[i]
            if first_at[a] == -1:
                first_at[a] = i
            if targetTemps[i] < a:
                bad = True
        if bad:
            inp.append(-1)
            continue

        by_target = [[] for _ in range(count + 1)]
        for i in range(count):
            if currentTemps[i] != targetTemps[i]:
                by_target[targetTemps[i]].append(i)

        switches = []
        impossible = False
        for t in range(1, count + 1):
            group = by_target[t]
            if not group:
                continue
            s = first_at[t]
            if s == -1:
                impossible = True
                break
            for i in group:
                switches.append("%d %d" % (s + 1, i + 1))
                s = i
        inp.append(-1 if impossible else switches)

outputfile = "warm_up_output.txt"
with open(outputfile, 'w') as f:
    for ctr, val in enumerate(inp, 1):
        if val == -1:
            f.write("Case #%d: -1\n" % ctr)
        elif val:
            f.write("Case #%d: %d\n" % (ctr, len(val)))
            f.write("\n".join(val) + "\n")
        else:
            f.write("Case #%d: 0\n" % ctr)

print(f'Total Time: {time.time() - start:.3f} seconds')