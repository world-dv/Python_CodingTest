import sys
r, c = map(int, sys.stdin.readline().split())
n = int(input())


def findMax(arr):
    answer = 0
    for i in range(len(arr)-1):
        answer = max(answer, arr[i] - arr[i+1])
    return answer


row = [0, r]
col = [0, c]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x:
        row.append(y)
    else:
        col.append(y)
row = sorted(row, reverse=True)
col = sorted(col, reverse=True)
print(findMax(row) * findMax(col))
