N = int(input())
answer = 0
for _ in range(N):
    x = 0
    a, b, c = map(int, input().split())
    if a == b == c:
        x = 10000 + a * 1000
    elif a == b != c:
        x = 1000 + a * 100
    elif b == c != a:
        x = 1000 + b * 100
    elif a == c != b:
        x = 1000 + c * 100
    else:
        x = max(a, b, c) * 100
    answer = max(answer, x)
print(answer)
