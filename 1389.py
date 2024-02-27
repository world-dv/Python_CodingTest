from collections import deque, defaultdict
import sys
N, M = map(int, input().split())
graph = defaultdict(list)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)


def bfs(start, visit):
    q = deque()
    q.append(start)
    visit[start] = 1
    total = [0 for _ in range(N+1)]

    while q:
        friend = q.popleft()
        for f in graph[friend]:
            if not visit[f]:
                visit[f] = 1
                total[f] = total[friend] + 1
                q.append(f)
    return sum(total)


min_value = 100000
min_idx = 0
for i in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    a = bfs(i, visited)
    if a < min_value:
        min_value = a
        min_idx = i
print(min_idx)
