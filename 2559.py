import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
temperature = list(map(int, sys.stdin.readline().rstrip().split()))
answer = []

start = 0
end = 0
cash = 0
while end < n:
    cash += temperature[end]
    if end - start + 1 == k:
        answer.append(cash)
        cash -= temperature[start]
        start += 1
        end += 1
    else:
        end += 1

print(max(answer))
