import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
    r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if r == 0:
        if r1 == r2:
            answer = -1
        else:
            answer = 0
    else:
        if r1 + r2 == r or abs(r1 - r2) == r:
            answer = 1
        elif r1 + r2 > r > abs(r1 - r2):
            answer = 2
        else:
            answer = 0

    print(answer)
