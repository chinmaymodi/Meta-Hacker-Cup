import time
from math import isqrt
start = time.time()

file = "nfactorful_input.txt"

LIMIT = 10**7
is_prime = bytearray(b"\x01") * (LIMIT + 1)
is_prime[0:2] = b"\x00\x00"
for p in range(2, isqrt(LIMIT) + 1):
    if is_prime[p]:
        is_prime[p*p::p] = bytes(len(range(p*p, LIMIT + 1, p)))

sieve = bytearray(is_prime)
plus_one = bytes((v + 1) % 256 for v in range(256))
pos = is_prime.find(1, 2)
while 0 < pos <= LIMIT // 2:
    sieve[2*pos::pos] = sieve[2*pos::pos].translate(plus_one)
    pos = is_prime.find(1, pos + 1)

output = []

with open(file, 'r') as f:
    n = int(f.readline())
    values = [list(map(int, f.readline().split())) for _ in range(n)]
    output = [str(sieve.count(c, a, b + 1)) for a, b, c in values]

outputfile = "nfactorful_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in output:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')