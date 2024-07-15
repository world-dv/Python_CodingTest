from collections import deque


def calculate(x):
    total = 0
    for t in range(1, len(x)):
        total += abs(x[t - 1] - x[t])
    return total


n = int(input())
arr = list(map(int, input().split()))
q = deque()
q2 = deque()
arr = sorted(arr)
for i in range(len(arr) // 2):
    a = arr.pop(0)
    b = arr.pop(-1)
    q.append(a)
    q.append(b)
    q2.append(b)
    q2.append(a)
if arr:
    c = arr.pop()
    q.append(c)
    q2.append(c)

q_max = 0
cnt = 0
while cnt < n:
    q_max = max(q_max, calculate(q))
    q.appendleft(q.pop())
    cnt += 1

cnt = 0
while cnt < n:
    q_max = max(q_max, calculate(q2))
    q2.appendleft(q2.pop())
    cnt += 1
print(q_max)
