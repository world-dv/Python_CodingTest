T = int(input())
for _ in range(T):
    arr = list(input().split())
    x = float(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == '@':
            x *= 3
        elif arr[i] == '%':
            x += 5
        elif arr[i] == '#':
            x -= 7
    print('{:.2f}'.format(x))
