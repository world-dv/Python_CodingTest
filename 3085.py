import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(n)]


def findLong():
    max_cnt = 0
    for i in range(n):
        cnt_r = 1
        cnt_c = 1
        for j in range(1, n):
            if graph[i][j-1] == graph[i][j]:
                cnt_r += 1
                max_cnt = max(max_cnt, cnt_r)
            else:
                cnt_r = 1
            if graph[j-1][i] == graph[j][i]:
                cnt_c += 1
                max_cnt = max(max_cnt, cnt_c)
            else:
                cnt_c = 1
    return max_cnt


answer = 0
for i in range(n):
    for j in range(n):
        # 오른쪽
        if j + 1 < n:
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
            answer = max(findLong(), answer)
            graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
        # 아래
        if i + 1 < n:
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
            answer = max(findLong(), answer)
            graph[i][j], graph[i + 1][j] = graph[i + 1][j], graph[i][j]
print(answer)
