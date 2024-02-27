from collections import defaultdict
n = int(input())
n1, n2 = map(int, input().split())
m = int(input())

global answer
graph = defaultdict(list)
visited = [0 for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
answer = 0
cnt = 0


def dfs(start, end, cnt):
    global answer
    if start == end:
        answer = cnt
    for x in graph[start]:
        if not visited[x]:
            visited[x] = 1
            dfs(x, end, cnt + 1)


dfs(n1, n2, cnt)
if answer == 0:
    print(-1)
else:
    print(answer)
