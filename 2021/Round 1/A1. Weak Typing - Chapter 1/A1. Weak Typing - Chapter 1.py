import time
start = time.time()

file = "weak_typing_chapter_1_input.txt"

output = []

def solve(test_string):
    starter = ''
    switches = 0
    test_set = {'X', 'O'}
    for character in test_string:
        if character in test_set:
            if starter == '':
                starter = character
            else:
                if starter != character:
                    switches += 1
                    starter = character
    return str(switches)


with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        f.readline()
        input_string = f.readline().strip()
        output.append(solve(input_string))

outputfile = "weak_typing_chapter_1_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
