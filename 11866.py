from collections import deque

N, K = map(int, input().split())
q = deque()
for i in range(1, N+1):
    q.append(i)
answer = []
idx = 1
while q:
    a = q.popleft()
    if idx == K:
        answer.append(a)
        idx = 1
    else:
        q.append(a)
        idx += 1

print('<'+', '.join(list(map(str, answer)))+'>', end='')
