import sys
from collections import defaultdict
N = int(sys.stdin.readline().rstrip())
X = list(map(int, sys.stdin.readline().rstrip().split()))
y = list(set(X))
y.sort()

dic = defaultdict(list)
for i in range(len(y)):
    dic[y[i]].append(i)
for i in X:
    print(dic[i][0], end=' ')
