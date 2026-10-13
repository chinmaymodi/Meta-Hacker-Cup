import time
start = time.time()

from functools import cmp_to_key

file = "studious_student_input.txt"
ans = []
with open(file, 'r') as f:
    f.readline()
    for line in f.readlines():
        ans.append(''.join(sorted(line.split()[1:], key=cmp_to_key(lambda a, b: -1 if a + b < b + a else (1 if a + b > b + a else 0)))))

outputfile = "studious_student_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')