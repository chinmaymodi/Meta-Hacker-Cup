import time
start = time.time()
file = "peg_game_input.txt"
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
        missingPegs = {}
        for r, c in holes:
            if r not in missingPegs:
                missingPegs[r] = set()
            missingPegs[r].add(2*c if r % 2 == 0 else 2*c + 1)
        score = {2 * target + 1: 1}
        #the 'rows' value is always odd
        row = rows - 2
        while row >= 0:
            newScore = {}
            # if row is odd, this is the intermediate row
            # i.e., first and last two elements are X,
            l, r = (2, 2*cols - 2) if row % 2 == 1 else (1, 2*cols - 1)
            for i in range(l, r, 2):
                if i in score:
                    newScore[i] = score[i]
                else:
                    temp = 0
                    if row % 2 == 0 and (i == l or i == r-2):
                        if i == l:
                            temp = score.get(i + 1, 0)
                        else:
                            temp = score.get(i - 1, 0)
                    else:
                        temp = (score.get(i - 1, 0) + score.get(i + 1, 0)) / 2.0
                    if temp != 0:
                        newScore[i] = temp
            # additionally, for any missing pegs in the current row, we also need to calculate
            if row in missingPegs:
                for c in missingPegs[row]:
                    newScore[c] = score.get(c, 0)
            score = newScore
            #print('score for row', row,'is', score)
            row -= 1
        #print(line, score)
        ans.append(max(score.items(), key=lambda item: item[1]))



outputfile = "peg_game_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + str(val[0]//2) + ' ' + f"{int(val[1] * 1e6 + 0.5) / 1e6:.6f}" + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')