t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    total = 0
    for _ in range(n):
        cnt = 0
        cx, cy, r = map(int, input().split())
        if (cx - x1) ** 2 + (cy - y1) ** 2 <= r ** 2:
            cnt += 1
        if (cx - x2) ** 2 + (cy - y2) ** 2 <= r ** 2:
            cnt += 1
        if cnt == 1:
            total += 1
    print(total)
