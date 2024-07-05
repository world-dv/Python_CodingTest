n = int(input())
for _ in range(n):
    arr = []
    p = int(input())
    for _ in range(p):
        c, name = input().split()
        arr.append([int(c), name])
    arr = sorted(arr, reverse=True)
    print(f'{arr[0][1]}')
