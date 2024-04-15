from collections import deque
import sys
N = int(sys.stdin.readline().rstrip())

q = deque()
for i in range(N):
    arr = sys.stdin.readline().rstrip().split()
    x = -1
    if arr[0] == 'push':
        q.append(arr[1])
        continue
    elif arr[0] == 'pop':
        if q:
            x = q.popleft()
    elif arr[0] == 'size':
        x = len(q)
    elif arr[0] == 'empty':
        if q:
            x = 0
        else:
            x = 1
    elif arr[0] == 'front':
        if q:
            x = q[0]
    elif arr[0] == 'back':
        if q:
            x = q[-1]
    print(x)

