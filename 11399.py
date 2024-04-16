N = int(input())
number = list(map(int, input().split()))
number.sort()

arr = [0] * N
arr[0] = number[0]
for i in range(1, N):
    arr[i] = arr[i-1] + number[i]
print(sum(arr))
