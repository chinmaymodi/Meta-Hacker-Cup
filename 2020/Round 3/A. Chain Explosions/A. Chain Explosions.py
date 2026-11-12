import time
start = time.time()

from bisect import bisect_right

degree_to_chain_count_map = [0, 0]
for i in range(2, 2001):
    degree_to_chain_count_map.append(i*(i-1))
# print(degree_to_chain_count_map[:5])

def solve(needed_chain_count):
    answer = []
    while needed_chain_count > 0:
        index_to_insert = bisect_right(degree_to_chain_count_map, needed_chain_count)-1
        answer.append(index_to_insert)
        needed_chain_count -= degree_to_chain_count_map[index_to_insert]
    # at this point, answer holds the DEGREE count of all star centers
    # need to subtract 2 from every inner star, 1 from every outer star
    if len(answer) > 1:
        for i in range(len(answer)):
            answer[i] -= 2 if 0 < i < len(answer)-1 else 1
    # print('answer', answer)
    star_centers = {}
    next_index = len(answer) + 1
    total = 0
    for i in range(1, len(answer)+1):
        star_centers[i] = [next_index, next_index + answer[i-1]-1]
        next_index += answer[i-1]
        total = next_index-1
    # for i in star_centers:
    #     print(i, star_centers[i])
    return_value = f'{total} {total-1}\n'
    for i in range(2, len(answer)+1):
        return_value += f'{i-1} {i}\n'
    for center in star_centers:
        for leaf in range(star_centers[center][0], star_centers[center][1]+1):
            return_value += f'{center} {leaf}\n'
    return return_value

file = "chain_explosions_input.txt"

output = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        ans = solve(int(f.readline()))
        output.append(str(ans))


outputfile = "chain_explosions_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val)
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')