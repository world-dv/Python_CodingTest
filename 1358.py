w, h, x, y, p = map(int, input().split())
total = 0
for _ in range(p):
    a, b = map(int, input().split())
    if x <= a <= x + w and y <= b <= y + h:
        total += 1
    elif pow(x - a, 2) + pow(y - b + h / 2, 2) <= pow(h / 2, 2):
        total += 1
    elif pow(x - a + w, 2) + pow(y - b + h / 2, 2) <= pow(h / 2, 2):
        total += 1
print(total)
