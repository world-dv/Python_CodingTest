import sys
n = int(sys.stdin.readline())

graph = [[0 for _ in range(1001)] for _ in range(1001)]
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    x, y, w, h = arr[i]
    for j in range(x, x+w):
        graph[j][y:y+h] = [i+1] * h

for i in range(1, n+1):
    cash = 0
    for j in range(1001):
        cash += graph[j].count(i)
    print(cash)
