import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = 1000000001
visit = [0 for _ in range(n)]


def dfs(idx, a, b):
    global arr, answer, visit
    answer = min(answer, abs(a - b))
    for i in range(idx+1, n):
        if not visit[i]:
            visit[i] = 1
            dfs(i, a * arr[i][0], b + arr[i][1])
            visit[i] = 0


for j in range(n):
    visit[j] = 1
    dfs(j, arr[j][0], arr[j][1])
    visit[j] = 0
print(answer)
