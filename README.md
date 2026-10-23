# Meta Hacker Cup Solutions

My solutions to Meta Hacker Cup (formerly Facebook Hacker Cup) problems, written in Python 3.

**16 problems solved**

## Structure

The repo is organized by year, then round, then problem. For example, the most recently solved problem:

- [2013](2013/)
  - [Qualification Round](2013/Qualification%20Round/)
    - [A. Beautiful Strings](2013/Qualification%20Round/A.%20Beautiful%20Strings/)

Each problem folder contains the solution script plus its input and output files. Every folder has a README describing the problem and approach.

## Progress

| Year | Round | Time | Solved |
|------|-------|------|--------|
| [2011](2011/) | [Qualification Round](2011/Qualification%20Round/) | ~0.501s | 3/3 |
| [2011](2011/) | [Round 1A](2011/Round%201A/) | ~0.019s | 2/3 |
| [2011](2011/) | [Round 1B](2011/Round%201B/) | ~1.026s | 3/3 |
| [2012](2012/) | [Qualification Round](2012/Qualification%20Round/) | ~0.005s | 1/3 |
| [2013](2013/) | [Qualification Round](2013/Qualification%20Round/) | ~0.003s | 1/3 |
| [2014](2014/) | [Qualification Round](2014/Qualification%20Round/) | ~6.011s | 3/3 |
| [2014](2014/) | [Round 1](2014/Round%201/) | ~0.001s | 1/4 |
| [2025](2025/) | [Practice Round](2025/Practice%20Round/) | ~1.8s | 1/5 |
| [2025](2025/) | [Round 1](2025/Round%201/) | ~0.001s | 1/6 |
| **Total** | | **~9.367s** | **16/33** |

## Running

Each script reads its own input file (the filename is hardcoded in the script) and writes its output file alongside it:

```
python "A. Double Squares.py"
```

Run from inside the problem folder. For example, `A. Double Squares.py` reads `double_squares_input.txt` and writes `double_squares_output.txt`.