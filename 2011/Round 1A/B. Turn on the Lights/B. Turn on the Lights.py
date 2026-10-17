import time

start = time.time()

file = "turn_on_the_lights_input.txt"

ans = []

def run_guess(matrix, r, c, fullValue, guess):
    tempMatrix = matrix.copy()
    cost = guess.bit_count()
    tempMatrix[0] ^= guess ^ ((guess << 1) & fullValue) ^ (guess >> 1)
    if r > 1:
        tempMatrix[1] ^= guess
    for i in range(1, r):
        aboveRowOff = tempMatrix[i - 1] ^ fullValue
        tempMatrix[i - 1] ^= aboveRowOff
        tempMatrix[i] ^= aboveRowOff ^ ((aboveRowOff << 1) & fullValue) ^ (aboveRowOff >> 1)
        if i + 1 < r:
            tempMatrix[i + 1] ^= aboveRowOff
        cost += aboveRowOff.bit_count()
    return tempMatrix[-1], cost


def solve_guesses(changes, target, c):
    basis = {}
    no_change = []
    for k in range(c):
        value, combo = changes[k], 1 << k
        while value:
            top_bit = value.bit_length() - 1
            if top_bit in basis:
                value ^= basis[top_bit][0]
                combo ^= basis[top_bit][1]
            else:
                basis[top_bit] = (value, combo)
                break
        if value == 0:
            no_change.append(combo)

    rest, guess = target, 0
    while rest:
        top_bit = rest.bit_length() - 1
        if top_bit in basis:
            rest ^= basis[top_bit][0]
            guess ^= basis[top_bit][1]
        else:
            return None, None
    return guess, no_change


def calc(r, c, matrix):
    fullValue = (1 << c) - 1
    start_bottom, _ = run_guess(matrix, r, c, fullValue, 0)
    changes = [run_guess(matrix, r, c, fullValue, 1 << k)[0] ^ start_bottom for k in range(c)]
    winner, no_change = solve_guesses(changes, fullValue ^ start_bottom, c)
    if winner is None:
        return -1
    ans = float('inf')
    for subset in range(1 << len(no_change)):
        guess = winner
        for j in range(len(no_change)):
            if subset >> j & 1:
                guess ^= no_change[j]
        bottom, cost = run_guess(matrix, r, c, fullValue, guess)
        if bottom == fullValue:
            ans = min(ans, cost)
    return ans if ans != float('inf') else -1


with open(file, 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        rows, cols = map(int, f.readline().split())
        grid = []
        for _ in range(rows):
            grid.append(f.readline().strip())
        if rows < cols:
            rows, cols = cols, rows
            grid = [''.join(col) for col in zip(*grid)]
        grid = [int(row.replace('X', '1').replace('.', '0'), 2) for row in grid]
        ans.append(str(calc(rows, cols, grid)))


outputfile = "turn_on_the_lights_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')