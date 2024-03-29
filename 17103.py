from sys import stdin
arr = [1] * 1000001
arr[0], arr[1] = 0, 0

for i in range(2, 1000001):
    if arr[i]:
        for j in range(2 * i, 1000001, i):
            arr[j] = 0

T = int(stdin.readline().rstrip())
for _ in range(T):
    N = int(stdin.readline().rstrip())
    answer = 0
    for i in range(2, (N // 2) + 1):
        if arr[i] and arr[N - i]:
            answer += 1
    print(answer)
