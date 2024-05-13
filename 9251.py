import sys
n = '0' + sys.stdin.readline().rstrip()
m = '0' + sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(m))] for _ in range(len(n))]

for i in range(1, len(n)):
    for j in range(1, len(m)):
        if n[i] == m[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[len(n)-1][len(m)-1])
