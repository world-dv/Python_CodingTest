import sys
n, k = map(int, sys.stdin.readline().split())
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= arr[i][0]:
            dp[i][j] = max(dp[i-1][j], arr[i][1] + dp[i-1][j - arr[i][0]])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][k])
