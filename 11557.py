from collections import defaultdict
T = int(input())

for _ in range(T):
    N = int(input())
    dic = defaultdict(str)
    for _ in range(N):
        a, b = input().split()
        dic[int(b)] = a
    print(dic[max(dic)])
