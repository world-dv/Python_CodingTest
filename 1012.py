from collections import deque

T = int(input())


for t in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(N)] for _ in range(M)]

    for k in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1


    def bfs(a, b):
        q = deque()
        q.append([a, b])
        graph[a][b] = 0

        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        while q:
            x, y = q.popleft()

            for i, j in zip(dx, dy):
                nx, ny = x + i, y + j

                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = 0
                        q.append([nx, ny])


    answer = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                answer += 1
                bfs(i, j)
    print(answer)
