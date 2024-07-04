n = int(input())

arr = []
for _ in range(n):
    arr.append(input().split())
arr = sorted(arr, key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(f'{arr[-1][0]}\n{arr[0][0]}')
