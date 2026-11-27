"""Second Second Meaning - my own solution.

Reads from standard input and writes to standard output.
"""

import sys
from itertools import product


def make_codewords(first, amount):
    """Return `amount` short codewords that are safe with `first`."""
    answer = []

    for letters in product(".-", repeat=10):
        word = "".join(letters)

        # Keep the whole code prefix-free.
        if word.startswith(first) or first.startswith(word):
            continue

        answer.append(word)
        if len(answer) == amount:
            break

    if len(answer) != amount:
        raise RuntimeError("not enough safe codewords")

    return answer


def solve(text):
    parts = text.split()
    if not parts:
        return ""

    t = int(parts[0])
    pos = 1
    lines = []

    for case in range(1, t + 1):
        n = int(parts[pos])
        first = parts[pos + 1]
        pos += 2

        lines.append(f"Case #{case}:")
        lines.extend(make_codewords(first, n - 1))

    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))
