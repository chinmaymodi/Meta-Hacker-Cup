import time
start = time.time()

file = "fighting_the_zombies_input.txt"

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        number_of_zombies, square_side_length = list(map(int, f.readline().split()))
        zombies = []
        for _ in range(number_of_zombies):
            zombies.append(tuple(map(int, f.readline().split())))
        bits = [1 << index for index in range(number_of_zombies)]
        x_masks = []
        for left, _ in zombies:
            right = left + square_side_length
            mask = 0
            for index, z in enumerate(zombies):
                if left <= z[0] <= right:
                    mask |= bits[index]
            x_masks.append(mask)
        y_masks = []
        for _, top in zombies:
            bottom = top - square_side_length
            mask = 0
            for index, z in enumerate(zombies):
                if bottom <= z[1] <= top:
                    mask |= bits[index]
            y_masks.append(mask)
        squares = {x_mask & y_mask for x_mask in x_masks for y_mask in y_masks}
        answer = 0
        squares = sorted(squares, key=lambda m: m.bit_count(), reverse=True)
        maximal_squares = []
        for square in squares:
            if any((square & ~big) == 0 for big in maximal_squares):
                continue
            maximal_squares.append(square)
        for i in range(len(maximal_squares)):
            a = maximal_squares[i]
            pa = a.bit_count()
            if 2 * pa <= answer:
                break
            for j in range(i, len(maximal_squares)):
                b = maximal_squares[j]
                if pa + b.bit_count() <= answer:
                    break
                count = (a | b).bit_count()
                if count > answer:
                    answer = count
        ans.append(str(answer))

outputfile = "fighting_the_zombies_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
