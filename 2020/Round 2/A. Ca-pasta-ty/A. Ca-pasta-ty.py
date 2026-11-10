import time
start = time.time()

def main():

    from itertools import repeat

    file = "capastaty_input.txt"

    output = []

    with (open(file, 'r') as f):
        t = int(f.readline())
        for _ in range(t):
            n, k = list(map(int, f.readline().strip().split()))
            s_series = list(map(int, f.readline().strip().split()))
            As, Bs, Cs, Ds = list(map(int, f.readline().strip().split()))
            x_series = list(map(int, f.readline().strip().split()))
            Ax, Bx, Cx, Dx = list(map(int, f.readline().strip().split()))
            y_series = list(map(int, f.readline().strip().split()))
            Ay, By, Cy, Dy = list(map(int, f.readline().strip().split()))
            must_remove = 0
            must_add = 0
            may_remove = 0
            may_add = 0
            for i in range(k):
                si = s_series[i]
                xi = x_series[i]
                yi = y_series[i]
                if si < xi:
                    must_add += xi - si
                    may_add += xi + yi - si
                elif si > xi+yi:
                    must_remove += si - xi - yi
                    may_remove += si - xi
                else:
                    may_add += yi - (si - xi)
                    may_remove += si - xi
            s2, s1 = s_series[-2], s_series[-1]
            x2, x1 = x_series[-2], x_series[-1]
            y2, y1 = y_series[-2], y_series[-1]
            for _ in repeat(None, n - k):
                s2, s1 = s1, (As * s2 + Bs * s1 + Cs) % Ds
                x2, x1 = x1, (Ax * x2 + Bx * x1 + Cx) % Dx
                y2, y1 = y1, (Ay * y2 + By * y1 + Cy) % Dy

                a = s1 - x1
                if a < 0:
                    must_add -= a
                    may_add += y1 - a
                elif a > y1:
                    must_remove += a - y1
                    may_remove += a
                else:
                    may_add += y1 - a
                    may_remove += a
            ans = 0
            if must_remove > may_add:
                ans = -1
            elif must_add > may_remove:
                ans = -1
            else:
                ans = max(must_add, must_remove)
            output.append(str(ans))



    outputfile = "capastaty_output.txt"
    with open(outputfile, 'w') as f:
        ctr = 1
        for val in output:
            f.write("Case #" + str(ctr) + ": " + val + "\n")
            ctr += 1
    print(f'Total Time: {time.time() - start:.3f} seconds')
main()