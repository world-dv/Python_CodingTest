n, k = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(input()))

answer = 0
for i in range(n-1, -1, -1):
    answer += k // A[i]
    k %= A[i]
print(answer)
