import sys
import math
N = sys.stdin.readline().rstrip()
answer = [0 for i in range(10)]
for i in N:
    answer[int(i)] += 1

if answer[6] > answer[9]:
    answer[6] = answer[9] + math.ceil((answer[6] - answer[9]) / 2)
elif answer[9] > answer[6]:
    answer[9] = answer[6] + math.ceil((answer[9] - answer[6]) / 2)

print(max(answer))
