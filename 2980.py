import sys

N, L = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

t = 0
pre = 0
for i in range(N):
    D, R, G = arr[i]
    t += (D - pre)
    if t % (R + G) <= R:
        t += (R - t % (R + G))
    pre = D
print(t + L - pre)
