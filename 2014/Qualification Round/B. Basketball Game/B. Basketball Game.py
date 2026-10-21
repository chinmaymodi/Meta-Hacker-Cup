import time
start = time.time()

from heapq import heappush, heappop

file = "basketball_game_input.txt"

output = []
with open(file, 'r') as f:
    test_cases = int(f.readline())
    for _ in range(test_cases):
        players = []
        n, m, p = map(int, f.readline().split())
        for _ in range(n):
            line = f.readline().split()
            name, shot_percentage, height = (lambda s: (s[0], int(s[1]), int(s[2])))(line)
            players.append([0, -shot_percentage, -height, name])
        players.sort()
        # print(players)
        team1 = players[::2]
        team2 = players[1::2]
        active1 = team1[p-1::-1]
        team1 = team1[p:]
        active2 = team2[p-1::-1]
        team2 = team2[p:]
        for i in range(len(active1)):
            active1[i][1] *= -1
            active1[i][2] *= -1
            active2[i][1] *= -1
            active2[i][2] *= -1
        # print("At start, players are %s" % (' '.join(sorted([p[3] for p in active1 + active2]))))
        for minute in range(m):
            for i in range(len(active1)):
                active1[i][0] -= 1
                active2[i][0] -= 1
            # print(active1, active2)
            # do not need to heapify again since we add 1 minute to ALL active times.
            # so the relative order stays the same, heap is still valid
            negtime1, negshotpc1, negheight1, name1 = heappop(active1)
            negtime2, negshotpc2, negheight2, name2 = heappop(active2)
            heappush(team1, [-negtime1, -negshotpc1, -negheight1, name1])
            heappush(team2, [-negtime2, -negshotpc2, -negheight2, name2])
            outtime1, outshotpc1, outheight1, outname1 = heappop(team1)
            outtime2, outshotpc2, outheight2, outname2 = heappop(team2)
            heappush(active1, [-outtime1, -outshotpc1, -outheight1, outname1])
            heappush(active2, [-outtime2, -outshotpc2, -outheight2, outname2])
            # print("After minute %d, players are %s" % (minute, ' '.join(sorted([p[3] for p in active1 + active2]))))
            # input()
        names = sorted([p[3] for p in active1 + active2])
        output.append(' '.join(names))


outputfile = "basketball_game_output.txt"
with open(outputfile, 'w') as f:
    for ind, val in enumerate(output, 1):
        f.write("Case #" + str(ind) + ": " + str(val) + "\n")
print(f'Total Time: {time.time() - start:.3f} seconds')