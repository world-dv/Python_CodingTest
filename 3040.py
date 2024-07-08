from itertools import combinations
answer = []
arr = [int(input()) for _ in range(9)]
for x in combinations(arr, 7):
    if sum(x) == 100:
        answer = x
        break
print('\n'.join(list(map(str,answer))))
