import time
start = time.time()

from functools import cache

file = "new_years_resolution_input.txt"

ans = []

g_p, g_c, g_f = 0, 0, 0
pcf_arr = []

def bitmask(pcf_array, target_array):
    n = len(pcf_array)
    for i in range(1, 1 << n):
        p, c, f = 0, 0, 0
        for j in range(n):
            if (i >> j) & 1:
                p += pcf_array[j][0]
                c += pcf_array[j][1]
                f += pcf_array[j][2]
        if p == target_array[0] and c == target_array[1] and f == target_array[2]:
            return 'yes'
    return 'no'

def backtracking(remaining_p, remaining_c, remaining_f, index):
    if remaining_p == 0 and remaining_c == 0 and remaining_f == 0:
        return 'yes'
    if index == len(pcf_arr):
        return 'no'
    if remaining_p < 0 or remaining_c < 0 or remaining_f < 0:
        return 'no'
    
    if backtracking(remaining_p - pcf_arr[index][0], remaining_c - pcf_arr[index][1], remaining_f - pcf_arr[index][2], index + 1) == 'yes':
        return 'yes'

    return backtracking(remaining_p, remaining_c, remaining_f, index + 1)

@cache
def memoized_dp(remaining_p, remaining_c, remaining_f, index):
    if remaining_p == 0 and remaining_c == 0 and remaining_f == 0:
        return 'yes'
    if index == len(pcf_arr):
        return 'no'
    if remaining_p < 0 or remaining_c < 0 or remaining_f < 0:
        return 'no'

    if memoized_dp(remaining_p - pcf_arr[index][0], remaining_c - pcf_arr[index][1], remaining_f - pcf_arr[index][2], index + 1) == 'yes':
        return 'yes'
    return memoized_dp(remaining_p, remaining_c, remaining_f, index + 1)

usemethod = 'b'
with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        g_p, g_c, g_f = map(int, f.readline().split(' '))
        n = int(f.readline())
        pcf_arr = []
        for _ in range(n):
            pcf_arr.append(list(map(int, f.readline().split(' '))))
        
        if usemethod == 'a':
            a = bitmask(pcf_arr, [g_p, g_c, g_f])
        elif usemethod == 'b':
            a = backtracking(g_p, g_c, g_f, 0)
        elif usemethod == 'c':
            memoized_dp.cache_clear()
            a = memoized_dp(g_p, g_c, g_f, 0)
        
        ans.append(a)

outputfile = "new_years_resolution_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
