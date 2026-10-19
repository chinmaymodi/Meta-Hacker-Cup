import time
start = time.time()

from collections import Counter

file = "alphabet_soup_input.txt"

neededDict = Counter('HACKERCUP')

def calc(letterDict):
    return min((letterDict.get(l, 0)//neededDict[l]) for l in neededDict)

inp = []
with open(file, 'r') as f:
    f.readline()
    for line in f.readlines():
        sentence = line.strip()
        lettersDict = Counter([i for i in sentence])
        inp.append(lettersDict)

outputfile = "alphabet_soup_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in inp:
        f.write("Case #" + str(ctr) + ": " + str(calc(val)) + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')