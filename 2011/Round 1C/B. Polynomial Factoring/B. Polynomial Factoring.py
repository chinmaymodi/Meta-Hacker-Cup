import time
start = time.time()

file = "polynomial_factoring_input.txt"

def solve(lhs, rhs):
    ll = len(lhs)
    lr = len(rhs)
    if ll > lr:
        return "no solution"
    degree = lr - ll
    answer = []
    while degree >= 0:
        c = rhs[-1]
        a = lhs[-1]
        multiplier = c//a
        if rhs[-1] != lhs[-1]*multiplier:
            return "no solution"
        for i in range(1, ll+1):
            rhs[-i] -= lhs[-i]*multiplier
        answer.append(multiplier)
        degree -= 1
        rhs.pop()
    if any(i != 0 for i in rhs):
        return "no solution"
    return " ".join(map(str, reversed(answer)))


output = []

with open(file, 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        target_polynomial = list(map(int, f.readline().split()))[1:]
        one_polynomial = list(map(int, f.readline().split()))[1:]
        output.append(solve(one_polynomial, target_polynomial))

outputfile = "polynomial_factoring_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')