arr = list(map(int, input().split()))

arr = sorted(arr)
if arr[0] + arr[1] > arr[2]:
    print(sum(arr))
else:
    print(2 * (arr[0] + arr[1]) - 1)
