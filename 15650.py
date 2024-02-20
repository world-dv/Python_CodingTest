N, M = map(int, input().split())


def printResult(x):
    for i in x:
        print(i, end=' ')
    print()


def dfs(start, visit):
    if len(start) == M:
        printResult(start)
        return

    for i in range(N):
        if not visit[i] and int(start[-1]) < i+1:
            visit[i] = 1
            dfs(start+str(i+1), visit)
            visit[i] = 0


visited = [0 for _ in range(N)]
for i in range(N):
    if not visited[i]:
        visited[i] = 1
        dfs(str(i+1), visited)
        visited[i] = 0
