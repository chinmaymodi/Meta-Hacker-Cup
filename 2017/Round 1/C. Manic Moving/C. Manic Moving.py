import time
start = time.time()

file = "manic_moving_input.txt"

ans = []

INF = float('inf')


def floyd(cm, n):
    rng = range(n)
    for k in rng:
        ck = cm[k]
        for i in rng:
            ci = cm[i]
            base = ci[k]
            if base == INF:
                continue
            for j in rng:
                v = base + ck[j]
                if v < ci[j]:
                    ci[j] = v


def solve(towns, city_map, family_starts, family_ends):
    count = len(family_starts)

    # precompute every leg distance once per family
    reach_next = [0] * count
    deliver_held = [0] * count
    deliver_own = [0] * count
    pick_next = [0] * count
    here_to_next = [0] * count
    drop_older = [0] * count

    for t in range(count):
        st = family_starts[t]
        en = family_ends[t]
        if t == 0:
            here = city_map[0]
        else:
            here = city_map[family_ends[t - 1]]
        reach_next[t] = here[st]
        deliver_held[t] = here[en]
        deliver_own[t] = city_map[st][en]
        if t + 1 < count:
            nxt = family_starts[t + 1]
            pick_next[t] = city_map[st][nxt]
            here_to_next[t] = here[nxt]
            drop_older[t] = city_map[nxt][en]

    # four flat state lists, indexed by families handled
    dp0 = [INF] * (count + 1)
    dp1 = [INF] * (count + 1)
    dp2 = [INF] * (count + 1)
    dp3 = [INF] * (count + 1)
    dp0[0] = 0

    for t in range(count):
        a0 = dp0[t]
        a1 = dp1[t]
        a2 = dp2[t]
        a3 = dp3[t]

        if a0 != INF:
            v = a0 + reach_next[t]
            if v < a2:
                a2 = v
        if a1 != INF:
            v = a1 + deliver_held[t]
            if v < dp0[t + 1]:
                dp0[t + 1] = v
            if t + 1 < count:
                v = a1 + here_to_next[t]
                if v < a3:
                    a3 = v
        if a2 != INF:
            v = a2 + deliver_own[t]
            if v < dp0[t + 1]:
                dp0[t + 1] = v
            if t + 1 < count:
                v = a2 + pick_next[t]
                if v < a3:
                    a3 = v
        if a3 != INF and t + 1 < count:
            v = a3 + drop_older[t]
            if v < dp1[t + 1]:
                dp1[t + 1] = v

        dp2[t] = a2
        dp3[t] = a3

        if a0 == INF and a1 == INF and a2 == INF and a3 == INF:
            break

    final = dp0[count]
    return -1 if final == INF else final


with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        towns, roads, num_families = list(map(int, f.readline().split()))
        city_map = [[float('inf') for _ in range(towns)] for _ in range(towns)]
        family_starts = [None for _ in range(num_families)]
        family_ends = [None for _ in range(num_families)]
        for i in range(towns):
            city_map[i][i] = 0
        for _ in range(roads):
            one_side, other_side, gas_cost = list(map(int, f.readline().split()))
            one_side -= 1
            other_side -= 1
            if city_map[one_side][other_side] > gas_cost:
                city_map[one_side][other_side] = gas_cost
                city_map[other_side][one_side] = gas_cost
        for i in range(num_families):
            s, d = list(map(int, f.readline().split()))
            family_starts[i] = s-1
            family_ends[i] = d-1
        floyd(city_map, towns)
        ans.append(str(solve(towns, city_map, family_starts, family_ends)))


outputfile = "manic_moving_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
