from collections import defaultdict
T = int(input())


for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    graph = defaultdict(int)
    visited = defaultdict(int)
    answer = 0
    for i, j in enumerate(arr):
        graph[i+1] = j


    def dfs(s):
        start = s
        while True:
            nt = graph[s]
            if start != nt:
                visited[nt] = 1
                s = nt
            else:
                break


    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            answer += 1
            dfs(i)
    print(answer)
