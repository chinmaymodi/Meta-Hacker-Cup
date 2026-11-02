import time
start = time.time()

from heapq import heapify, heappush, heappop

file = "pie_progress_input.txt"

ans = []

TAX = tuple(2 * i + 1 for i in range(300))

with (open(file, 'r') as f):
    t = int(f.readline())
    for _ in range(t):
        days, daily_pies = map(int, f.readline().split())
        total_expense = 0
        pie_queue = []
        day_heaps = []
        consumed = [0] * days
        for _ in range(days):
            todays_pies = list(map(int, f.readline().split()))
            heapify(todays_pies)
            day_heaps.append(todays_pies)
            heappush(pie_queue, (todays_pies[0] + 1, len(day_heaps) - 1))
            cost, day_index = heappop(pie_queue)
            total_expense += cost
            prices = day_heaps[day_index]
            heappop(prices)
            consumed[day_index] += 1
            if prices:
                heappush(pie_queue, (prices[0] + TAX[consumed[day_index]], day_index))
        ans.append(str(total_expense))


outputfile = "pie_progress_output.txt"
with open(outputfile, 'w') as f:
    ctr = 1
    for val in ans:
        f.write("Case #" + str(ctr) + ": " + val + "\n")
        ctr += 1
print(f'Total Time: {time.time() - start:.3f} seconds')
