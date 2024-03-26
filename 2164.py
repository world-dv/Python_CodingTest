from collections import deque

N = int(input())
q = deque()
for i in range(1, N+1):
    q.append(i)
if N > 1:
    while True:
        q.popleft()
        if len(q) == 1:
            break
        if q:
            q.append(q.popleft())
print(q[0])
