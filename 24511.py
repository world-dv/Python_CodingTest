import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
CN = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))[::-1]
for i in range(N):
    if not A[i]:
        B.append(arr[i])
B.reverse()
print(' '.join(list(map(str, B[:CN]))))
