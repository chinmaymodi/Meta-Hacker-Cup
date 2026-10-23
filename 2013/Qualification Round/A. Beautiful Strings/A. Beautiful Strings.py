import time
start = time.time()

from collections import Counter

file = "beautiful_strings_input.txt"

ans = []
with open(file, 'r') as f:
    f.readline()
    for line in f.readlines():
        letters = sorted(Counter(line.lower()).items(), key = lambda x: x[1], reverse = True)
        # print(letters)
        beauty = 26
        total_beauty = 0
        for l, count in letters:
            if not ord('a') <= ord(l) <= ord('z'):
                continue
            total_beauty += beauty * count
            beauty -= 1
        ans.append(total_beauty)

outputfile = "beautiful_strings_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + str(val) + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')