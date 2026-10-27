import time
start = time.time()

file = "interception_input.txt"

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for i in range(t):
        degree = int(f.readline())
        for _ in range(degree+1):
            f.readline()
        ans.append('1\n'+str(0.0) if degree % 2 == 1 else '0')
outputfile = "interception_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
