import time

start = time.time()

file = "slot_machine_hacker_input.txt"
def getAllPossibleSecrets(currentSecret, nextSecret):
    ansSet = set()
    for temp in range(currentSecret, 10000001, 1000):
        nextTemp = (temp * 5402147 + 54321) % 10000001
        if nextTemp % 1000 == nextSecret:
            ansSet.add(nextTemp)
    return ansSet

ans = []
with open(file, 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        obs, *values = map(int, f.readline().split())
        #print(obs, values)
        if obs == 1:
            ans.append("Not enough observations")
        else:
            possibleStarterSecretsSet = getAllPossibleSecrets(values[0], values[1])
            #print("Possible secrets that result in value 2 from value 1 are:", possibleStarterSecretsSet)
            for i in range(1, len(values)-1):
                currentSecret = values[i]
                nextSecret = values[i+1]
                #print('Trying to find possible secrets that result in value', nextSecret, 'from value', currentSecret)
                newSecrets = set()
                for previousSecret in possibleStarterSecretsSet:
                    possibleNextNumber = (previousSecret * 5402147 + 54321) % 10000001
                    if possibleNextNumber % 1000 == nextSecret:
                        newSecrets.add(possibleNextNumber)
                #print("Possible secrets that result in value", nextSecret, "from value", currentSecret, "are:", newSecrets)
                possibleStarterSecretsSet = newSecrets
            if not possibleStarterSecretsSet:
                ans.append("Wrong machine")
            elif len(possibleStarterSecretsSet) == 1:
                # here, we create next 10 and add to the ans as an entry
                currentSecret = possibleStarterSecretsSet.pop()
                tempAns = []
                for _ in range(10):
                    nextSecret = (currentSecret * 5402147 + 54321) % 10000001
                    tempAns.append(nextSecret % 1000)
                    currentSecret = nextSecret
                ans.append(" ".join(map(str, tempAns)))
            else:
                ans.append("Not enough observations")


outputfile = "slot_machine_hacker_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')