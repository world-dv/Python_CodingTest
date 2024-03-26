from collections import deque
import sys
N = int(input())
q = deque()
for _ in range(N):
    a = sys.stdin.readline().split()
    x = -1
    if a[0] == 'push':
        q.append(int(a[1]))
        continue
    elif a[0] == 'pop':
        if q:
            x = q.popleft()
    elif a[0] == 'size':
        x = len(q)
    elif a[0] == 'empty':
        if q:
            x = 0
        else:
            x = 1
    elif a[0] == 'front':
        if q:
            x = q[0]
    elif a[0] == 'back':
        if q:
            x = q[-1]
    print(x)
