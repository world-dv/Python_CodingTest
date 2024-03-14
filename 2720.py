N = int(input())

for _ in range(N):
    x = int(input())

    print(x // 25, end=' ')
    x %= 25
    print(x // 10, end=' ')
    x %= 10
    print(x // 5, end=' ')
    x %= 5
    print(x)
