import time

file1 = "second_friend_input.txt"
file2 = "second_second_friend_sample_input.txt"
files = [file1, file2]
outputfile1 = "second_friend_output.txt"
outputfile2 = "second_second_friend_output.txt"
output_files = [outputfile1, outputfile2]

def solve(test_grid):
    rows = len(test_grid)
    cols = len(test_grid[0])
    trees = set()
    rocks = []
    removal = []
    nbs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    nbc = [[0 for _ in range(cols)] for _ in range(rows)]
    seen = set()
    for i in range(rows):
        for j in range(cols):
            if test_grid[i][j] == '#':
                rocks.append((i, j))
                continue
            if test_grid[i][j] == '^':
                trees.add((i, j))
            else:
                test_grid[i][j] = '^'
            for dx, dy in nbs:
                if 0 <= i+dx < rows and 0 <= j+dy < cols and test_grid[i+dx][j+dy] != '#':
                    nbc[i][j] += 1
            if nbc[i][j] < 2:
                removal.append((i, j))
                seen.add((i, j))
    if rows == 1 or cols == 1 or not removal:
        if trees and removal:
            return 'Impossible'
        else:
            if rows == 1 or cols == 1:
                return "Possible\n" + "\n".join("".join(row).replace("^", ".") for row in test_grid)
            else:
                return "Possible\n" + "\n".join("".join(row).replace(".", "^") for row in test_grid)
    while removal:
        x, y = removal.pop()
        test_grid[x][y] = '.'
        for dx, dy in nbs:
            p = x+dx
            q = y+dy
            if (p, q) not in seen and 0 <= p < rows and 0 <= q < cols and test_grid[p][q] != '#':
                nbc[p][q] -= 1
                if nbc[p][q] < 2:
                    removal.append((p, q))
                    seen.add((p, q))
    for i, j in trees:
        if test_grid[i][j] == '.':
            return 'Impossible'
    return "Possible\n" + "\n".join("".join(row) for row in test_grid)


def main():
    for file, outputfile in zip(files, output_files):
        start = time.time()
        output_array = []
        with (open(file, 'r') as f):
            t = int(f.readline())
            for _ in range(t):
                input_grid = []
                r, c = list(map(int, f.readline().split()))
                for _ in range(r):
                    input_grid.append(list(f.readline().strip()))
                output_array.append(solve(input_grid))


        with open(outputfile, 'w') as f:
            for ctr, val in enumerate(output_array, start=1):
                f.write("Case #" + str(ctr) + ": " + val + "\n")
                ctr += 1
        print(f'Total Time: {time.time() - start:.3f} seconds')
if __name__ == '__main__':
    main()