import time
start = time.time()

file = "ethan_searches_for_a_string_input.txt"

ans = []

with (open(file, 'r') as f):
    t = int(f.readline())
    for i in range(t):
        input_string = f.readline().strip()
        # now, if the string contains a repetition of the first letter in it, then it can be tripped up
        # as in, ABACUS -> ABABACUS
        # then, the strings will match until ABA, and then on the next B, it will reset
        # ignoring that the 2nd AB is part of the match
        # which is a mistake in the naive substring function
        # So if for some index i > 0, we have
        # input_string[i] == input_string[0]
        # and very importantly,
        # input_string[:i] + input_string[:-i] != input_string
        # then we can return input_string[:i] + input_string
        # otherwise it is not possible
        entered = False
        for i in range(1, len(input_string)):
            if input_string[0] == input_string[i]:
                if input_string[:i] + input_string[:-i] != input_string:
                    ans.append(input_string[:i] + input_string)
                    entered = True
                break
        if not entered:
            ans.append("Impossible")

outputfile = "ethan_searches_for_a_string_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
