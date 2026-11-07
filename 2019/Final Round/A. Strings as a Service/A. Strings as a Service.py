import time
start = time.time()

file = "strings_as_a_service_input.txt"

ans = []

matches = [0]
i = 1
while True:
    z = (i*(i+1))//2
    if z > 100000:
        break
    matches.append(z)
    i += 1

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        palindrome_count = int(f.readline().strip())
        output = ''
        strt = 'A'
        end = len(matches) - 1
        while palindrome_count > 0:
            if matches[end] <= palindrome_count:
                output += strt*end
                palindrome_count -= matches[end]
                strt = chr(ord(strt) + 1)
            else:
                end -= 1
        ans.append(output)


outputfile = "strings_as_a_service_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
