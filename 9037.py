def addCandy(x):
    for a in range(len(x)):
        x[a] = x[a] + x[a] % 2
    return x


def check(x):
    s = sum(x) // len(x)
    arr = [a for a in x if a == s]
    return len(arr) == len(x)


t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    c = addCandy(c)
    total = 0
    while True:
        if check(c):
            break
        arr = [b // 2 for b in c]
        for i in range(len(c)):
            arr[(i + 1) % len(c)] += c[i % len(c)] // 2
            arr[(i + 1) % len(c)] = arr[(i + 1) % len(c)] + arr[(i + 1) % len(c)] % 2
        total += 1
        c = arr
    print(total)
