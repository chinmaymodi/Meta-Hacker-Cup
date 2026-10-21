import time
start = time.time()

file = "labelmaker_input.txt"

output = []
with open(file, 'r') as f:
    count = int(f.readline())
    for _ in range(count):
        letters, n = (lambda x: (x[0], int(x[1])))(f.readline().split())
        ans = ''
        d = len(letters)
        while n:
            n, idx = divmod(n-1, d)
            ans += letters[idx]
        output.append(''.join(reversed(ans)))

outputfile = "labelmaker_output.txt"
with open(outputfile, 'w') as f:
    for ind, val in enumerate(output, 1):
        f.write("Case #" + str(ind) + ": " + str(val) + "\n")
print(f'Total Time: {time.time() - start:.3f} seconds')