import sys
from collections import deque
n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


def bfs(start_x, start_y):
    q = deque()
    q.append([start_x, start_y])
    graph[start_x][start_y] = 0
    cnt = 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        x, y = q.popleft()

        for mx, my in zip(dx, dy):
            nx = mx + x
            ny = my + y
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny]:
                    graph[nx][ny] = 0
                    q.append([nx, ny])
                    cnt += 1
    return cnt


answer = []
total = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            total += 1
            answer.append(bfs(i, j))
answer.sort()

print(total)
for i in answer:
    print(i)
