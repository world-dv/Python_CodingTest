n = int(input())
arr = list(map(int, input().split()))
k = -1

'''
a b c d e를 뒤에서 부터 e -> a로 탐색
c < d라면 c를 기준으로 e -> d로 탐색해 c보다 큰 수를 찾아 swap
원래 c 인덱스 이후 부터 오름차순 정렬
'''

for i in range(len(arr) - 2, -1, -1):
    if arr[i] < arr[i+1]:
        k = i
        break
x = -1
for i in range(len(arr) - 1, k, -1):
    if arr[i] > arr[k]:
        x = i
        break

arr[k], arr[x] = arr[x], arr[k]
answer = arr[:k+1] + sorted(arr[k+1:])
if k == -1:
    print(-1)
else:
    print(' '.join(list(map(str, answer))))
