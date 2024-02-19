N, M = map(int, (input().split()))
x, y, d = map(int, (input().split()))

graph = []

for i in range(N):
    graph.append(list(map(int, (input().split()))))

# d == 0 : 북쪽, 1 : 동쪽, 2 : 남쪽, 3 : 서쪽
#        (-1,0)
# (0,-1) (0,0), (0,1)
#        (1,0)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def setPos(x):
    if x == 0:
        return 3
    return x - 1


def setBackPos(x):
    if x <= 1:
        return x + 2
    return x - 2


cnt = 0
answer = 1
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[x][y] = 1
while True:
    d_left = setPos(d)
    nx, ny = x + dx[d_left], y + dy[d_left]

    if 0 <= nx < N and 0 <= ny < M:
        if not visited[nx][ny] and not graph[nx][ny]:
            visited[nx][ny] = 1
            x, y = nx, ny
            cnt = 0
            answer += 1
            d = d_left
            continue
        else:
            cnt += 1
            d = d_left

        if cnt == 4:
            nx, ny = x + dx[setBackPos(d)], y + dy[setBackPos(d)]
            if graph[nx][ny]:
                break
            x, y = nx, ny
            cnt = 0
print(answer)
