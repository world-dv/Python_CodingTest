n = int(input())
for i in range(1, n+1):
    score = list(map(int, input().split()))
    print(f'Class {i}')
    score = sorted(score[1:], reverse=True)
    gap = 0
    for x in range(len(score)-1):
        gap = max(gap, score[x] - score[x + 1])
    print(f'Max {score[0]}, Min {score[-1]}, Largest gap {gap}')
