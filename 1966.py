t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    stack = []
    for i in range(len(arr)):
        stack.append([arr[i], i])
    arr = sorted(arr, reverse=True)
    cnt = 0
    while stack:
        x, y = stack.pop(0)
        if arr[cnt] > x:
            stack.append([x, y])
        else:
            cnt += 1
            if y == m:
                break
    print(cnt)
