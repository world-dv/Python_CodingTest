n = int(input())
arr = list(map(int, input().split()))
answer = []

"""
1. a b c d e 일 때 e -> a로 탐색
2. c > d일 경우 c와 d, e 중 뒤에서 c보다 작은 수를 찾아 swap
3. 그 후 원래 c의 인덱스 이후 배열을 내림차순으로 정렬
"""
k = -1
for i in range(len(arr) - 2, -1, -1):
    if arr[i] > arr[i + 1]:
        k = i
        break
x = -1
for j in range(len(arr) - 1, k, -1):
    if arr[j] < arr[k]:
        x = j
        break
arr[k], arr[x] = arr[x], arr[k]
answer = arr[:k + 1] + sorted(arr[k + 1:], reverse=True)

if k != -1:
    print(' '.join(map(str, answer)))
else:
    print(-1)
