N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]
idx = K - 1
answer = []
while True:
    answer.append(str(arr.pop(idx)))
    if not arr:
        break
    idx = (idx + (K-1)) % len(arr)

print('<' + ', '.join(answer) + '>')
