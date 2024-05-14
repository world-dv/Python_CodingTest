import sys
n = int(sys.stdin.readline())
graph = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            graph[i][j] = 1

answer = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for i in range(1, 101):
    for j in range(1, 101):
        if graph[i][j] == 1:
            cnt = 0
            for a, b in zip(dx, dy):
                nx, ny = i + a, j + b
                if graph[nx][ny]:
                    cnt += 1
            if cnt == 2: # 모서리일 때
                answer += 2
            elif cnt == 3: # 직선일 때
                answer += 1
print(answer)
