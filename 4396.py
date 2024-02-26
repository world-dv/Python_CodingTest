N = int(input())
graph = [input() for _ in range(N)]
user = [[-1 for _ in range(N)] for _ in range(N)]
for i in range(N):
    u = input()
    for j in range(N):
        if u[j] == 'x':
            user[i][j] = 0

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [0, 1, -1, 1, -1, 1, 0, -1]

for i in range(N):
    for j in range(N):
        if graph[i][j] == '*' and user[i][j] == 0:
            # 모든 지뢰 칸이 *로 표시
            for a in range(N):
                for b in range(N):
                    if graph[a][b] == '*':
                        user[a][b] = -2
            continue

        if user[i][j] == 0:
            cnt = 0
            for a, b in zip(dx, dy):
                x, y = i + a, j + b
                if 0 <= x < N and 0 <= y < N:
                    cnt += 1 if graph[x][y] == '*' else 0
            user[i][j] = cnt

for i in user:
    for j in i:
        if j == -1:
            print('.', end='')
        elif j == -2:
            print('*', end='')
        else:
            print(j, end='')
    print()
