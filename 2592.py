from collections import defaultdict

total = 0
dic = defaultdict(int)
for _ in range(10):
    i = int(input())
    dic[i] += 1
    total += i

arr = sorted(dic, key=lambda x: dic[x], reverse=True)
print(f'{total // 10}\n{arr[0]}')
