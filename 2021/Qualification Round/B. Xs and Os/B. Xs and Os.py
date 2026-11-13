import time
start = time.time()

file = "xs_and_os_input.txt"

output = []

def solve(test_grid):
    n = len(test_grid)
    smallest_replacement_count = float('inf')
    replacement_set = set()
    for i in range(n):
        row = test_grid[i]
        if 'O' in row:
            continue
        places = tuple(sorted(i*n + j for j, v in enumerate(row) if v == '.'))
        if len(places) < smallest_replacement_count:
            smallest_replacement_count = len(places)
            replacement_set = {places}
        elif len(places) == smallest_replacement_count:
            replacement_set.add(places)
    for i, col in enumerate(zip(*test_grid)):
        if 'O' in col:
            continue
        places = tuple(sorted(j*n + i for j, v in enumerate(col) if v == '.'))
        if len(places) < smallest_replacement_count:
            smallest_replacement_count = len(places)
            replacement_set = {places}
        elif len(places) == smallest_replacement_count:
            replacement_set.add(places)
    return_value = 'Impossible' if not replacement_set else str(smallest_replacement_count) + ' ' + str(len(replacement_set))
    return return_value


with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        n = int(f.readline())
        grid = [f.readline().strip() for _ in range(n)]
        ans = solve(grid)
        output.append(ans)

outputfile = "xs_and_os_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
