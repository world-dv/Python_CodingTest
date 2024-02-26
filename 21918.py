N, M = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        arr[b-1] = c
    elif a == 2:
        for x in range(b-1, c):
            arr[x] = int(not arr[x])
    elif a == 3:
        for x in range(b-1, c):
            arr[x] = 0
    else:
        for x in range(b-1, c):
            arr[x] = 1
print(' '.join(map(str, arr)))
