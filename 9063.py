N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

if N == 1:
    print(0)
else:
    a = sorted(arr, key=lambda x: x[0])
    b = sorted(arr, key=lambda x: x[1])
    print((a[-1][0] - a[0][0]) * (b[-1][1] - b[0][1]))

