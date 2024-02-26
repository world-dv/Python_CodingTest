n = int(input())

if n == 1:
    print(3)
else:
    dp = [0 for _ in range(n)]
    dp[0], dp[1] = 3, 7

    for i in range(2, n):
        dp[i] = (dp[i-2] + dp[i-1] * 2) % 9901
    print(dp[n-1])
