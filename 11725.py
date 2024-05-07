from collections import deque
import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visit = [1, 1] + [0] * (n-1)
q = deque()
q.append(1)
while q:
    a = q.popleft()

    for i in graph[a]:
        if not visit[i]:
            visit[i] = a
            q.append(i)

print('\n'.join(map(str, visit[2:])))
