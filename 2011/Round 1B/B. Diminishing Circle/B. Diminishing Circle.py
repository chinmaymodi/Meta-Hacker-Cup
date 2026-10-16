import time
start = time.time()

file = "diminishing_circle_input.txt"
ans = []

def g(n, k):
    if n == 1:
        return 0
    if k == 1:
        return n - 1
    if n < k:
        result = 0
        for i in range(2, n + 1):
            result = (result + k) % i
        return result
    stack = []
    while n >= k:
        stack.append(n)
        n = n - n // k
    result = 0
    for i in range(2, n + 1):
        result = (result + k) % i
    for n in reversed(stack):
        temp = result
        if temp < n % k:
            result = temp - n % k + n
        else:
            result = (k * (temp - n % k)) // (k - 1)
    return result

with open(file, 'r') as f:
    n = int(f.readline())
    for i in range(n):
        n, k = map(int, f.readline().split(' '))
        #print(i, n, k)
        tempAns = g(n, k+1) + 1
        ans.append(str(tempAns))

outputfile = "diminishing_circle_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
