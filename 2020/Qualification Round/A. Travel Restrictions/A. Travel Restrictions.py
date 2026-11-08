import time
start = time.time()

file = "travel_restrictions_input.txt"

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        n_count = int(f.readline())
        incoming = f.readline().strip()
        outgoing = f.readline().strip()
        airline_ans = [['N' for _ in range(n_count)] for _ in range(n_count)]
        for i in range(n_count):
            airline_ans[i][i] = 'Y'
            for j in range(i-1, -1, -1):
                #check incoming flights leftwards?
                if incoming[j] == 'Y' and outgoing[j+1] == 'Y':
                    airline_ans[i][j] = 'Y'
                else:
                    break
            for j in range(i+1, n_count):
                #check outgoing flights rightwards?
                if outgoing[j-1] == 'Y' and incoming[j] == 'Y':
                    airline_ans[i][j] = 'Y'
                else:
                    break
        output = ''
        for i in range(n_count):
            output += '\n' + ''.join(airline_ans[i])
        ans.append(output)

outputfile = "travel_restrictions_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
