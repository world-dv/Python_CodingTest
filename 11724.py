import sys
from collections import defaultdict, deque
N, M = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
visited = []


def bfs(start):
    q = deque()
    q.append(start)

    while q:
        s = q.popleft()
        for g in graph[s]:
            if g not in visited:
                visited.append(g)
                q.append(g)


cnt = 0
for x in range(N):
    if x not in visited:
        visited.append(x)
        bfs(x)
        cnt += 1
print(cnt)
