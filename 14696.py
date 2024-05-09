import sys
from collections import Counter
n = int(sys.stdin.readline())

answer = ''
for _ in range(n):
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    CardA = Counter(A[1:])
    CardB = Counter(B[1:])
    cash = ''
    for i in range(4, 0, -1):
        if i in CardA and i not in CardB:
            cash = 'A'
            break
        elif i in CardB and i not in CardA:
            cash = 'B'
            break
        elif i in CardA and i in CardB:
            if CardA[i] > CardB[i]:
                cash = 'A'
                break
            elif CardA[i] == CardB[i]:
                continue
            else:
                cash = 'B'
                break
    if cash == '':
        cash = 'D'
    answer += cash
print('\n'.join(answer))
