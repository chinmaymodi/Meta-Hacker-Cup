import time
start = time.time()

file = "ethan_traverses_a_tree_input.txt"

ans = []
with (open(file, 'r') as f):
    t = int(f.readline())
    for i in range(t):
        n, k = map(int, (f.readline().split()))

        left = [0] * (n + 1)
        right = [0] * (n + 1)

        for j in range(n):
            lc, rc = map(int, f.readline().split())
            left[j+1] = lc
            right[j+1] = rc
        pre = []
        stack = [1]
        while stack:
            u = stack.pop()
            if u == 0:
                continue
            pre.append(u)
            stack.append(right[u])
            stack.append(left[u])

        post = []
        stack1 = [1]
        stack2 = []
        while stack1:
            u = stack1.pop()
            if u:
                stack2.append(u)
                stack1.append(left[u])
                stack1.append(right[u])
        post = stack2[::-1]

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n):
            a, b = pre[i], post[i]
            ra, rb = find(a), find(b)
            if ra != rb:
                if size[ra] < size[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                size[ra] += size[rb]
        for i in range(1, n + 1):
            parent[i] = find(i)
        if len(set(parent[1:])) < k:
            ans.append("Impossible")
            continue

        labels = {}
        kcounter = 1
        for j in range(1, n + 1):
            r = parent[j]
            if r in labels:
                continue
            labels[r] = kcounter
            kcounter = min(kcounter + 1, k)
                
        ans.append(' '.join(str(labels[parent[j]]) for j in range(1, n + 1)))

outputfile = "ethan_traverses_a_tree_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')