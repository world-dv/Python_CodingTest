from collections import deque

M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]

for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1


def bfs(x, y):
    cnt = 1
    q = deque()
    q.append([x, y])
    graph[x][y] = 1

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while q:
        x, y = q.popleft()
        for i, j in zip(dx, dy):
            nx, ny = x + i, y + j
            if 0 <= nx < M and 0 <= ny < N:
                if not graph[nx][ny]:
                    graph[nx][ny] = 1
                    cnt += 1
                    q.append([nx, ny])
    return cnt


answer = []
count = 0
for i in range(M):
    for j in range(N):
        if not graph[i][j]:
            count += 1
            answer.append(bfs(i, j))
print(count)
print(' '.join(map(str, sorted(answer))))
