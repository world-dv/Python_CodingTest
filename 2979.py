abc = list(map(int, input().split()))
total = 0
arr = [0 for _ in range(101)]
for i in range(3):
    x, y = map(int, input().split())
    for j in range(x, y):
        arr[j] += 1
for i in range(len(arr)):
    if arr[i] != 0:
        total += arr[i] * abc[arr[i]-1]
print(total)
