import sys
L = int(sys.stdin.readline())
n = int(sys.stdin.readline())
cake = [0 for _ in range(L+1)]
long = 0
long_idx = 0
for i in range(1, n+1):
    x, y = map(int, sys.stdin.readline().split())
    if long < y - x:
        long = y - x
        long_idx = i
    for a in range(x, y+1):
        if not cake[a]:
            cake[a] = i
print(long_idx)
real_long = 0
real_long_idx = 0
for i in range(1, n+1):
    if real_long < cake.count(i):
        real_long = cake.count(i)
        real_long_idx = i
print(real_long_idx)
