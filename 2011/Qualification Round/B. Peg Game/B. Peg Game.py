import time
start = time.time()

file = "peg_game_sample_input.txt"
ans = []
with open(file, 'r') as f:
    f.readline()
    for line in f.readlines():
        # input is rows, columns, target hole, integer m, then m pairs of holes instead of pegs.
        data = list(map(int, line.split()))
        rows, cols, target, m = data[:4]
        holes = [
            (data[i], data[i + 1])
            for i in range(4, 4 + 2 * m, 2)
        ]
        targetcol = 2*target + 1
        print(targetcol)

outputfile = "peg_game_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in inp:
        f.write("Case #" + str(ctr) + ": " + '' + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')