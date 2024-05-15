import sys
n, k = map(int, sys.stdin.readline().split())
sit = [0 for _ in range(n)]
for i in range(n):
    x = int(sys.stdin.readline())
    sit[i] = x

start = 0
answer = 0
check = 0
for _ in range(n):
    if k == start:
        check = 1
        break
    start = sit[start]
    answer += 1
if check:
    print(answer)
else:
    print(-1)
