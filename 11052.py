N = int(input())
dp = [0] + list(map(int, input().split()))
for i in range(1, N+1):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j] + dp[j])
print(dp[N])
