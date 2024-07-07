t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr, reverse=True)
    total = arr[0]
    for i in range(m - 1):
        total += abs(arr[i] - arr[i + 1])
    total -= arr[-1]
    print(total)

