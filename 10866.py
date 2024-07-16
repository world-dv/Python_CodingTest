from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque()
result = []
for _ in range(n):
    x = list(sys.stdin.readline().split())
    a = -1
    if x[0] == "push_back":
        q.append(int(x[1]))
        continue
    elif x[0] == "push_front":
        q.appendleft(int(x[1]))
        continue
    elif x[0] == "front":
        if q:
            a = q[0]
    elif x[0] == "back":
        if q:
            a = q[-1]
    elif x[0] == "pop_front":
        if q:
            a = q.popleft()
    elif x[0] == "pop_back":
        if q:
            a = q.pop()
    elif x[0] == "size":
        a = len(q)
    elif x[0] == "empty":
        if q:
            a = 0
        else:
            a = 1
    result.append(a)
print('\n'.join(list(map(str, result))))
