from collections import deque
import sys
N = int(input())
q = deque()
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    x = -1
    if arr[0] == 1:
        q.appendleft(arr[1])
        continue
    elif arr[0] == 2:
        q.append(arr[1])
        continue
    elif arr[0] == 3:
        if q:
            x = q.popleft()
    elif arr[0] == 4:
        if q:
            x = q.pop()
    elif arr[0] == 5:
        x = len(q)
    elif arr[0] == 6:
        if q:
            x = 0
        else:
            x = 1
    elif arr[0] == 7:
        if q:
            x = q[0]
    elif arr[0] == 8:
        if q:
            x = q[-1]
    print(x)
