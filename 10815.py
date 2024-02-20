N = int(input())
sang = set(map(int, input().split()))
M = int(input())
card = list(map(int, input().split()))

for i, j in enumerate(card):
    if j in sang:
        print(1, end=' ')
    else:
        print(0, end=' ')
