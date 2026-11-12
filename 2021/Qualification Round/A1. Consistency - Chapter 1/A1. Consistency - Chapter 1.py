import time
start = time.time()

file = "consistency_chapter_1_input.txt"

output = []

def solve(test_string):
    orda = ord('A')
    vowels = set(ord(i)-orda for i in 'AEIOU')
    target_letters = [0 for _ in range(26)]
    for letter in test_string:
        ord_letter = ord(letter) - orda
        is_vowel = ord_letter in vowels
        #print('letter is', letter, 'and its ord is', ord_letter, 'and is it a vowel?', is_vowel)
        for i in range(26):
            if ord_letter == i:
                continue
            if (i in vowels and is_vowel) or (i not in vowels and not is_vowel):
                #print('YEAH')
                target_letters[i] += 2
            else:
                #print('NOPE')
                target_letters[i] += 1
    #print(test_string, target_letters)
    return min(target_letters)


with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        output.append(str(solve(f.readline().strip())))

outputfile = "consistency_chapter_1_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
