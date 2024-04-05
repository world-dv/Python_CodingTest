import sys
N = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
A = [0] * len(B)

for i in range(len(B)):
    A[i] = B[i] * (i+1)
print(A[0], end=' ')
for i in range(1, len(B)):
    print(A[i] - A[i-1], end=' ')
