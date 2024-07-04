m = int(input())
for _ in range(m):
    s = int(input())
    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        s += q * p
    print(s)
