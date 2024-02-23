from collections import deque
N, M = map(int, input().split())
graph = ['' for _ in range(N)]

for i in range(N):
    graph[i] = list(input())


def bfs(x, y):
    q = deque()
    q.append([x, y, 1])
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while q:
        x, y, cost = q.popleft()
        if x == N-1 and y == M-1:
            return cost
        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == '1':
                    graph[nx][ny] = '0'
                    q.append([nx, ny, cost+1])
    return -1


print(bfs(0, 0))
