T = int(input())
case = [int(input()) for _ in range(T)]
dp = [0 for i in range(max(case) + 1)]
dp[0], dp[1], dp[2] = 1, 1, 2

for i in range(3, len(dp)):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

for i in case:
    print(dp[i])
