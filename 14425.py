from collections import defaultdict
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

dic = defaultdict(int)
for _ in range(N):
    dic[sys.stdin.readline().rstrip()] = 0

for _ in range(M):
    x = sys.stdin.readline().rstrip()
    if x in dic:
        dic[x] += 1

answer = 0
for i in dic:
    answer += dic[i]
print(answer)
