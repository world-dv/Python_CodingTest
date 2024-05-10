import sys

c, r = map(int, sys.stdin.readline().rstrip().split())
k = int(sys.stdin.readline().rstrip())

if k == 1:
    print(1, 1)
elif c * r < k:
    print(0)
else:

    sit = [[0 for _ in range(c)] for _ in range(r)]
    # 0: 위, 1: 오, 2: 아, 3: 왼
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x, y = r - 1, 0
    pos = 0
    sit[x][y] = 1
    cnt = 2


    def changePos(p):
        p += 1
        if p == 4:
            return 0
        return p


    answer = [0, 0]
    while cnt <= c * r:
        nx, ny = x + dx[pos], y + dy[pos]
        if 0 <= nx < r and 0 <= ny < c:
            if not sit[nx][ny]:
                sit[nx][ny] = cnt
                x, y = nx, ny
                if cnt == k:
                    answer = [y + 1, r - x]
                    break
                cnt += 1
            else:
                pos = changePos(pos)
        else:
            pos = changePos(pos)

    print(f'{answer[0]} {answer[1]}')
