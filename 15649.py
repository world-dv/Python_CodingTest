N, M = map(int, input().split())

visited = [0 for _ in range(N)]


def dfs(start, visit):
    if M == len(start):
        for i in start:
            print(i, end=' ')
        print()
        return

    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            dfs(start + str(i+1), visit)
            visit[i] = 0
    return


for i in range(N):
    if not visited[i]:
        visited[i] = 1
        dfs(str(i+1), visited)
        visited[i] = 0
