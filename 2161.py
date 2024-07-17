from collections import deque
n = int(input())
q = deque([i for i in range(1, n+1)])
while True:
    print(q.popleft(), end=' ')
    if q:
        q.append(q.popleft())
    else:
        break
