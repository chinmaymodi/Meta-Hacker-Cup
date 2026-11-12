import time
start = time.time()

from collections import Counter, deque

file = "consistency_chapter_2_input.txt"

output = []

def solve(test_string, replacements):
    ord_a = ord('A')
    infi = float('inf')
    adjacency = [[] for _ in range(26)]
    for path in replacements:
        adjacency[ord(path[0])-ord_a].append(ord(path[1])-ord_a)
    counts = Counter(ord(letter) - ord_a for letter in test_string)
    costs = [0 for _ in range(26)]
    unreachable = [False for _ in range(26)]
    # one BFS per letter that actually appears in S, each node visited once
    for source, amount in counts.items():
        dist = [-1 for _ in range(26)]
        dist[source] = 0
        queue = deque([source])
        while queue:
            node = queue.popleft()
            next_dist = dist[node] + 1
            for neighbor in adjacency[node]:
                if dist[neighbor] < 0:
                    dist[neighbor] = next_dist
                    queue.append(neighbor)
        for target_letter in range(26):
            if target_letter == source:
                continue
            step = dist[target_letter]
            if step < 0:
                unreachable[target_letter] = True
            else:
                costs[target_letter] += step * amount
    best = infi
    for target_letter in range(26):
        if not unreachable[target_letter] and costs[target_letter] < best:
            best = costs[target_letter]
    return best if best < infi else -1

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        input_string = f.readline().strip()
        k = int(f.readline())
        paths = [f.readline().strip() for _ in range(k)]
        output.append(str(solve(input_string, paths)))

outputfile = "consistency_chapter_2_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
