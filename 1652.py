n = int(input())
arr = [list(input()) for _ in range(n)]
arr2 = [['' for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr2[i][j] = arr[j][abs(n - i - 1)]


def count(x):
    total = 0
    for i in x:
        a = ''.join(i).split('X')
        for j in a:
            if j.count('..') >= 1:
                total += 1
    return total


print(f'{count(arr)} {count(arr2)}')
