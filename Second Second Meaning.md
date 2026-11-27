# Second Second Meaning

My own answer for the version where every codeword I add may be at most 10 characters long.

## Problem in my words

I am given one codeword that must stay in the code. I must add enough other codewords so that the full set is unambiguous.

Unambiguous means that after all spaces are removed, a dot-dash string never has two different valid splits into codewords. A string having no valid split is fine. A string having two valid splits is not fine.

The given codeword can be up to 100 characters long. Every codeword I add must have length from 1 to 10.

## Key idea

I will make a prefix-free set.

Prefix-free means no codeword is the beginning of another codeword. Prefix-free code sets are unambiguous because scanning from left to right never gives a choice. At any position, either no codeword matches the remaining text, or exactly one codeword matches it.

I only need to avoid two bad situations:

- The given codeword is the beginning of one of my new words.
- One of my new words is the beginning of the given codeword.

## Construction

I only generate new words of length exactly 10.

Because every new word has the same length, no new word can be the beginning of another new word.

For each candidate new word, I skip it if:

- it starts with the given codeword, or
- the given codeword starts with it.

Then I take the first enough candidates.

There are 1024 dot-dash words of length 10. The most forbidden case is when the given codeword has length 1, which blocks 512 of them. That still leaves 512 usable words, and I never need more than 99. So this always works.

## Correctness

The new words all have length 10, so none is a prefix of another new word.

I skip any candidate that is a prefix of the given word, so no new word is a prefix of the given word.

I skip any candidate that starts with the given word, so the given word is not a prefix of any new word.

Therefore the full code is prefix-free.

Now suppose some dot-dash string had two different splits into codewords. Compare the first codeword in each split. Both are prefixes of the same string, so one must be a prefix of the other. Since the code is prefix-free, they must actually be the same word. Remove that first word and repeat the argument. Every word in both splits is the same, so the splits are not different. Contradiction.

So the produced code is unambiguous.

## Complexity

There are only 1024 possible length-10 words, and at most 99 are needed per test case. The work per case is constant.

## Sample note

The judge accepts any valid answer, so my output does not have to match the sample output. For the sample input, my script produces a different but valid set of codewords.
