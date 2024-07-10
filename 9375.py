from collections import defaultdict
t = int(input())
for _ in range(t):
    dic = defaultdict(list)
    n = int(input())
    for _ in range(n):
        wear, ty = input().split()
        dic[ty].append(wear)
    total = 1
    for d in dic:
        total *= (len(dic[d]) + 1)
    print(total - 1)
