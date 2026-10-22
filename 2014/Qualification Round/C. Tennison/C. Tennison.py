import os
import time
from concurrent.futures import ProcessPoolExecutor

file = "tennison_input.txt"
outputfile = "tennison_output.txt"


def solve_case(k, sun_win, rain_win, sun_prob, sun_up_amount, sun_up_prob, sun_down_amount, sun_down_prob):
    win_up = [0.0] * 1001
    win_stay = [0.0] * 1001
    lose_down = [0.0] * 1001
    lose_stay = [0.0] * 1001
    up = [0] * 1001
    down = [0] * 1001

    for p in range(1001):
        probability = p / 1000.0
        win = probability * sun_win + (1.0 - probability) * rain_win
        lose = 1.0 - win
        win_up[p] = win * sun_up_prob
        win_stay[p] = win * (1.0 - sun_up_prob)
        lose_down[p] = lose * sun_down_prob
        lose_stay[p] = lose * (1.0 - sun_down_prob)
        up[p] = min(1000, p + sun_up_amount)
        down[p] = max(0, p - sun_down_amount)

    reach = [[set() for _ in range(k)] for _ in range(k)]
    reach[0][0].add(sun_prob)

    for w in range(k):
        for l in range(k):
            current = reach[w][l]
            if not current:
                continue
            if w + 1 < k:
                target = reach[w + 1][l]
                for p in current:
                    target.add(up[p])
                    target.add(p)
            if l + 1 < k:
                target = reach[w][l + 1]
                for p in current:
                    target.add(down[p])
                    target.add(p)

    next_row = None
    for w in range(k - 1, -1, -1):
        row = [None] * k
        win_terminal = (w + 1 == k)
        for l in range(k - 1, -1, -1):
            loss_terminal = (l + 1 == k)
            win_child = None if win_terminal else next_row[l]
            loss_child = None if loss_terminal else row[l + 1]
            values = {}
            for p in reach[w][l]:
                if win_terminal:
                    win_up_value = 1.0
                    win_stay_value = 1.0
                else:
                    win_up_value = win_child[up[p]]
                    win_stay_value = win_child[p]
                if loss_terminal:
                    lose_down_value = 0.0
                    lose_stay_value = 0.0
                else:
                    lose_down_value = loss_child[down[p]]
                    lose_stay_value = loss_child[p]
                values[p] = (
                    win_up[p] * win_up_value
                    + win_stay[p] * win_stay_value
                    + lose_down[p] * lose_down_value
                    + lose_stay[p] * lose_stay_value
                )
            row[l] = values
        next_row = row

    return next_row[0][sun_prob]


def solve_worker(case):
    return solve_case(*case)


if __name__ == "__main__":
    start = time.time()

    cases = []
    with open(file, 'r') as f:
        test_cases = int(f.readline())
        for _ in range(test_cases):
            k, sun_win, rain_win, sun_prob, sun_up_amount, sun_up_prob, sun_down_amount, sun_down_prob = map(float, f.readline().split())
            cases.append((
                int(k),
                sun_win,
                rain_win,
                int(round(sun_prob * 1000)),
                int(round(sun_up_amount * 1000)),
                sun_up_prob,
                int(round(sun_down_amount * 1000)),
                sun_down_prob,
            ))

    workers = min(6, os.cpu_count() or 1)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        output = list(executor.map(solve_worker, cases, chunksize=1))

    with open(outputfile, 'w') as f:
        for ind, val in enumerate(output, 1):
            f.write("Case #" + str(ind) + ": " + f"{val:.6f}" + "\n")

    print(f'Total Time: {time.time() - start:.3f} seconds')
