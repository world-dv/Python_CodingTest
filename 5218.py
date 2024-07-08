t = int(input())
for _ in range(t):
    arr = []
    x, y = input().split()
    for i, j in zip(x, y):
        if ord(j) >= ord(i):
            arr.append(ord(j) - ord(i))
        else:
            arr.append(ord(j) + 26 - ord(i))
    print(f'Distances: {" ".join(list(map(str, arr)))}')
