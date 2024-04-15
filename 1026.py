N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
S = 0
for i, j in zip(A, B):
    S += i * j
print(S)
