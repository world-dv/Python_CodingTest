N, M = map(int, input().split())


def printResult(x):
    for i in x:
        print(i, end=' ')
    print()


def dfs(start):
    if len(start) == M:
        printResult(start)
        return

    for i in range(N):
        if int(start[-1]) <= i+1:
            dfs(start+str(i+1))


for i in range(N):
    dfs(str(i+1))
