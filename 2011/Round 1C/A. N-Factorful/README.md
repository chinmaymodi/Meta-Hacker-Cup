[Meta-Hacker-Cup](../../../) / [2011](../../) / [Round 1C](../) / A. N-Factorful

# A. N-Factorful

An integer is n-factorful when it has exactly $n$ distinct prime factors. Given $n$, $a$, and $b$, count the n-factorful integers in the closed interval $[a, b]$.

## Approach

Build a table for the number of distinct prime divisors of every $x$ up to $10^7$, then answer each query by counting the entries equal to $n$ in the requested range.

The table is built in two passes over a pair of bytearrays.

First, a normal sieve of Eratosthenes fills `is_prime`. The marking loop only reaches $\sqrt{10^7}$, but slice assignment writes zeros across the whole array, so `is_prime` is valid everywhere. Each prime is written with `is_prime[p*p::p] = bytes(...)`.

Second, `sieve = bytearray(is_prime)` seeds every prime at 1, which is its own one distinct prime factor, and every composite at 0. A 256-byte `plus_one` table maps each byte value to itself plus one, so `translate` can add one to a whole strided slice at C speed. `is_prime.find(1, pos)` walks the primes in C instead of scanning all $10^7$ indices in Python. For each prime $p \le 10^7 / 2$, the slice `sieve[2*p::p]` holds the multiples $2p, 3p, ...$, each of which gains one more distinct prime factor. The stride starts at $2p$ so the prime's seeded value is left alone. Primes above $10^7 / 2$ have no multiples left to touch and keep their seeded 1.

The two arrays are kept separate because the counting pass turns a composite such as 4 from 0 into 1, which would otherwise look like a prime to a later `find`.

Each query is then one call: `sieve.count(n, a, b + 1)`, with `b + 1` because the `count` end index is exclusive. `bytearray.count` runs in C, so all 50 queries together cost a few hundredths of a second. The largest omega value below $10^7$ is 8, so any query with $n = 9$ or $n = 10$ answers 0 automatically.

## Complexity

$O(N \log \log N)$ for the two sieve passes, where $N = 10^7$, with the increments done by `translate` at C speed. Each query is $O(N)$ in C via `count`. Space is $O(N)$ for the two bytearrays, about 20 MB.

## Time

~0.623 seconds.

Solved: 18 November 2026.

## Lessons

- Bulk bytearray operations are the fast path in Python. Slice assignment, `find`, `translate`, and `count` all run the heavy loop in C; the interpreter only makes a handful of calls around them. Keeping the sieve in a `bytearray` and using `translate` with a 256-byte lookup table turns roughly $10^7$ per-element additions into a few thousand C-level calls, which is what brings the build under a second.
- Match the structure to the query count. Each `count` is a single C scan over at most $10^7$ bytes, so with only 50 queries all of them together cost a few hundredths of a second. That is far cheaper than preprocessing an index. A posting list gives $O(\log N)$ lookups via `bisect`, but building it needs a Python loop over all $10^7$ values (about 3.5 s, more than five times the whole solution). Prefix sums have the same flaw. Indexing only pays when enough queries accumulate to amortize the build, which does not happen here.
- `bytearray.count(value, start, end)` takes an exclusive `end`, so an inclusive range $[a, b]$ needs `count(value, a, b + 1)`.