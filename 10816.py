from collections import Counter
import sys

N = int(sys.stdin.readline().rstrip())
card = Counter(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
have = list(map(int, sys.stdin.readline().rstrip().split()))
for i in have:
    if i in card:
        print(card[i], end=' ')
    else:
        print(0, end=' ')
