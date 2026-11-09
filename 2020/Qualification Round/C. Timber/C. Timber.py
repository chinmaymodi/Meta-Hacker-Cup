import time
start = time.time()

file = "timber_input.txt"

output = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        ans = 0
        on_the_left = {}
        tot = int(f.readline())
        trees = sorted([list(map(int, f.readline().split())) for _ in range(tot)])
        right_falls_at = {}
        left_falls_at = {}
        for position, height in trees:
            final_right_position = position + height
            new_length = right_falls_at.get(position, 0) + height
            if new_length > ans:
                ans = new_length
            right_falls_at[final_right_position] = max(new_length, right_falls_at.get(final_right_position, 0))
        for position, height in trees[::-1]:
            final_left_position = position - height
            new_length = right_falls_at.get(position, 0) + height
            if right_falls_at.get(final_left_position, 0) + new_length > ans:
                ans = new_length
            left_falls_at[final_left_position] = max(new_length, left_falls_at.get(final_left_position, 0))
        output.append(str(ans))


outputfile = "timber_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
