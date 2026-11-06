import time
start = time.time()

file = "leapfrog_ch_2_input.txt"

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        lilypads = f.readline().strip()
        b_count = lilypads.count('B')
        dot_count = lilypads.count('.')
        val = 'N'
        if (b_count >= 2 or b_count == dot_count) and dot_count > 0:
            val = 'Y'
        ans.append(val)

outputfile = "leapfrog_ch_2_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
