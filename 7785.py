from collections import defaultdict

N = int(input())
dic = defaultdict(str)
for _ in range(N):
    a, b = input().split()
    dic[a] = b
    if dic[a] == 'leave':
        del dic[a]

arr = sorted(dic, reverse=True)
print('\n'.join(arr))
