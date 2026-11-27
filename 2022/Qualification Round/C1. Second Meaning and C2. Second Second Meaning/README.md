[Meta-Hacker-Cup](../../../) / [2022](../../) / [Qualification Round](../) / C1. Second Meaning and C2. Second Second Meaning

# C1. Second Meaning and C2. Second Second Meaning

C1 is the version where generated codewords may be at most 10 characters. C2 allows up to 200. Given a count `N` and one codeword, generate N-1 more distinct codewords so the whole set is an unambiguous encoding: no sequence of dots and dashes may have two different parses.

A single README covers both problems because the script solves both input files with the same code. The two input files in this folder are identical. Both were uploaded and accepted.

## Approach

An unambiguous code is prefix-free: no codeword may be a prefix of another. It is enough to make every word the same length and keep only words that do not overlap by prefix with the given C1.

Precompute dot/dash words from binary numbers 0 to 1023, using 10 bits and mapping 0 to `.` and 1 to `-`. Every such word has length 10, so no two of them can be prefixes of each other. For each candidate word p, keep it when `not p.startswith(c1) and not c1.startswith(p)`. Those two checks remove every prefix relationship with the given word. Take the first N-1 kept words and print them.

At most 99 words are needed, and the first 1024 ten-bit words are more than enough. Technically, even 8-bit precounted words would have been fine, since we need at most 99 newer codewords, so any provided codeword would remove at most 128, and still leave us at least 128 valid options.

## Correctness

All printed words have length 10, so none is a prefix of another printed word. The two startswith tests guarantee that the given C1 is not a prefix of a printed word and that a printed word is not a prefix of C1. Therefore the full set is prefix-free, which is exactly the condition for an unambiguous encoding. An answer always exists, and the sweep finds one because at most 99 candidates are needed out of 1024.

## Complexity

Precompute is O(1) time and memory, done once at startup.

Each test case scans at most ~612 candidates, so it is O(1) time, effectively constant. Both prefix checks run on fixed-length words, so they do not scale with the length of C1. Output size is O(N) lines. Memory is O(1024) for the precomputed words plus O(len(C1)) for the input word.

## Time

~0.018 seconds.

This is the combined time for both input files in one run.

Solved: 27 November 2026.

## Lessons

- Equal length makes prefix-free automatic among generated words, so the only real work is comparing each candidate against the given C1.
- The safe test is two-sided: `p.startswith(c1)` catches C1 as a prefix, and `c1.startswith(p)` catches the candidate as a prefix of C1.
- Fixed 10-character words satisfy both versions at once, so one script can solve C1 and C2 without branching on the problem name.
