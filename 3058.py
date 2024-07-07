t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    min_n = max(arr)
    total = 0
    for i in arr:
        if i % 2 == 0:
            min_n = min(min_n, i)
            total += i
    print(f'{total} {min_n}')
