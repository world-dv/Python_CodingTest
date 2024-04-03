n = int(input())
x, y = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        x -= b
    elif a > b:
        y -= a
print(100 + x)
print(100 + y)
