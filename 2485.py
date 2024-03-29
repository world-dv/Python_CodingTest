import sys
from math import gcd
N = int(sys.stdin.readline().rstrip())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline().rstrip()))

x = arr[1] - arr[0]
for i in range(1, N-1):
    x = gcd(x, arr[i + 1] - arr[i])

print((arr[-1] - arr[0]) // x - (N-1))
