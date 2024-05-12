import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr2 = arr[::-1]
dp = [1] * n
dp2 = [1] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        if arr2[i] > arr2[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

answer = [0 for i in range(n)]
for i in range(n):
    answer[i] = dp[i] + dp2[n-i-1] - 1
print(max(answer))
