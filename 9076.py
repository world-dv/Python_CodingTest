t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    if max(arr[1:4]) - min(arr[1:4]) >= 4:
        print('KIN')
    else:
        print(sum(arr[1:4]))
