import sys
N = int(sys.stdin.readline().rstrip())
arr = [0] * 10001
for i in range(N):
    arr[int(sys.stdin.readline().rstrip())] += 1

for i in range(10001):
    if arr[i] > 0:
        for _ in range(arr[i]):
            sys.stdout.write(str(i) + '\n')
