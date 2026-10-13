# Meta Hacker Cup Solutions

My solutions to Meta Hacker Cup (formerly Facebook Hacker Cup) problems, written in Python 3.

## Structure

The repo is organized by year, then round, then problem:

```
2011/
  Qualification Round/
    A. Double Squares/
    B. Peg Game/
    C. Studious Student/
  Round 1B/
    A. Chess 2/
```

Each problem folder contains the solution script plus its input and output files. Every folder has a README describing the problem and approach.

## Progress

| Year | Round | Problems |
|------|-------|----------|
| 2011 | Qualification Round | 3 |
| 2011 | Round 1B | 1 |

## Running

Each script reads its own input file (the filename is hardcoded in the script) and writes its output file alongside it:

```
python "A. Double Squares.py"
```

Run from inside the problem folder. For example, `A. Double Squares.py` reads `double_squares_input.txt` and writes `double_squares_output.txt`.