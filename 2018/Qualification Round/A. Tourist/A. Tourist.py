import time
start = time.time()

file = "tourist_input.txt"

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for i in range(t):
        n, k, v = list(map(int, f.readline().split()))
        attractions_list = [f.readline().strip() for _ in range(n)]
        # If we imagine the attractions as looping from the end
        # Then the input can be treated as a circular list for picking the next k attractions to visit
        # Because we visit the least visited ones
        # So the structure is [0, 1, ...k, k+1, ...n-1, n, n+1...]
        # For the purpose of choosing which ones we visit
        # in visit 1, we visit [:k] attractions.
        # in visit 2, we visit [k:2k] attractions
        # in visit 3, we visit [2k:3k] attractions
        # ... in visit v, we visit [k*(v-1):k*v] attractions
        # so, need to get the index of k*(v-1) % n as well as the ending of k*v % n
        start_index = (k*(v-1)) % n
        end_index = (k*v) % n
        if start_index < end_index:
            ans.append(" ".join(attractions_list[start_index:end_index]))
        else:
            ans.append(" ".join(attractions_list[:end_index] + attractions_list[start_index:]))

outputfile = "tourist_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
