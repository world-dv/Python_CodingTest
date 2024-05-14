import sys
n = int(sys.stdin.readline().rstrip())
graph = [0 for _ in range(1001)]


limit_L = 0
high_L = 0
high_H = 0
for _ in range(n):
    L, H = map(int, sys.stdin.readline().rstrip().split())
    graph[L] = H
    if high_H < H:
        high_H = H
        high_L = L
    limit_L = max(L, limit_L)

cash = 0
for i in range(0, high_L):
    cash = max(cash, graph[i])
    graph[i] = cash
cash = 0
for i in range(limit_L, high_L, - 1):
    cash = max(cash, graph[i])
    graph[i] = cash

print(sum(graph))
