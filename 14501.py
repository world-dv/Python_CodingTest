N = int(input())

consult = []
for i in range(N):
    consult.append(list(map(int, input().split())))

dp = [0 for _ in range(N+1)]

for i in range(N):
    for j in range(i + consult[i][0], N+1):
        dp[j] = max(dp[j], dp[i] + consult[i][1])
print(dp[-1])
