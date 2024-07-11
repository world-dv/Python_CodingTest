from itertools import permutations

n = int(input())
arr = [i for i in range(1, n+1)]
for x in permutations(arr, n):
    print(' '.join(list(map(str, x))))
