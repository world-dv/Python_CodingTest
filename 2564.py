import sys
r, c = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

# 사각형 테두리를 한 줄로 잇는다. -> 절대 거리
# <- 1 -> <- 4 -> <- 2 -> <- 3 ->
# <- r -> <- c -> <- r -> <- c ->
# => 방향에 따라 전체 길이 - 위치 = 0,0부터 해당 지점까지 거리


def setPos(p, d):
    if p == 1:
        return d
    elif p == 2:
        return 2 * r + c - d
    elif p == 3:
        return 2 * r + 2 * c - d
    else:
        return r + d


cash = []
for _ in range(n):
    pos, dis = map(int, sys.stdin.readline().split())
    cash.append(setPos(pos, dis))

x, y = map(int, sys.stdin.readline().split())
current_pos = setPos(x, y)
total = 2 * r + 2 * c
answer = 0
for i in cash:
    dist = abs(current_pos - i)
    answer += min(dist, total - dist)
print(answer)
