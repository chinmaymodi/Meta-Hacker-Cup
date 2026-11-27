import time

file1 = "second_meaning_input.txt"
file2 = "second_second_meaning_input.txt"
files = [file1, file2]
outputfile1 = "second_meaning_output.txt"
outputfile2 = "second_second_meaning_output.txt"
output_files = [outputfile1, outputfile2]

precompute = []
for i in range(0, 1025):
    s = bin(i)[2:].rjust(10, '0')
    precompute.append(s.replace('0', '.').replace('1', '-'))

def solve(n, c1):
    pre = precompute
    answer_array = []
    i = 0
    for p in pre:
        if not p.startswith(c1) and not c1.startswith(p):
            i += 1
            answer_array.append(p)
            if i == n-1:
                break
    return '\n' + '\n'.join(answer_array)

def main():
    for file, outputfile in zip(files, output_files):
        start = time.time()
        output_array = []
        with (open(file, 'r') as f):
            for _ in range(int(f.readline())):
                n = int(f.readline())
                c1 = f.readline().strip()
                output_array.append(solve(n, c1))


        with open(outputfile, 'w') as f:
            for ctr, val in enumerate(output_array, start=1):
                f.write("Case #" + str(ctr) + ": " + val + "\n")
                ctr += 1
        print(f'Total Time: {time.time() - start:.3f} seconds')
if __name__ == '__main__':
    main()