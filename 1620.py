import sys
from collections import defaultdict
N, M = map(int, sys.stdin.readline().rstrip().split())
dogam = defaultdict(int)
dogam_idx = defaultdict(str)
for i in range(1, N+1):
    x = sys.stdin.readline().rstrip()
    dogam[x] = i
    dogam_idx[i] = x

for i in range(M):
    x = sys.stdin.readline().rstrip()
    if x.isdigit():
        print(dogam_idx[int(x)])
    else:
        print(dogam[x])
