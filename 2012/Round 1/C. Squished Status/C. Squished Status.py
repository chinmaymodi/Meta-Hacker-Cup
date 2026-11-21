import time
start = time.time()

file = "squished_status_input.txt"

MOD = 4207849484

def solve(high_char, compressed):
    n = len(compressed)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        if compressed[i] == '0':
            continue
        v = 0
        for j in range(i, n):
            v = v * 10 + (ord(compressed[j]) - 48)
            if v > high_char:
                break
            dp[j + 1] = (dp[j + 1] + dp[i]) % MOD
    return str(dp[n])

output_array = []
input_array = []
with open(file, 'r') as f:
    ln = int(f.readline())
    while len(input_array) < 2*ln:
        input_array.extend(f.readline().split())
    for k in range(0, 2*ln, 2):
        output_array.append(solve(int(input_array[k]), input_array[k+1]))

outputfile = "squished_status_output.txt"

with open(outputfile, 'w') as f:
    ctr = 1
    for val in output_array:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')