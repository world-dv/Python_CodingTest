from collections import deque, defaultdict

N, M, V = map(int, input().split())

graph = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a] = sorted(graph[a])
    graph[b] = sorted(graph[b])

visited = defaultdict()
visited2 = defaultdict()
for i in graph:
    visited[i] = 0
    visited2[i] = 0


def bfs(start, visit):
    q = deque()
    q.append(start)
    visit[start] = 1
    print(start, end=' ')

    while q:
        s = q.popleft()
        for g in graph[s]:
            if not visit[g]:
                visit[g] = 1
                print(g, end=' ')
                q.append(g)


def dfs(start):
    print(start, end=' ')
    visited2[start] = 1
    for g in graph[start]:
        if not visited2[g]:
            visited2[g] = 1
            dfs(g)


dfs(V)
print()
bfs(V, visited)
