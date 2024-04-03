from collections import defaultdict
n = int(input())
dic = defaultdict(int)
for i in ['Q1', 'Q2', 'Q3', 'Q4', 'AXIS']:
    dic[i] = 0

for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        dic['AXIS'] += 1
    elif x > 0 and y > 0:
        dic['Q1'] += 1
    elif x < 0 and y > 0:
        dic['Q2'] += 1
    elif x < 0 and y < 0:
        dic['Q3'] += 1
    elif x > 0 and y < 0:
        dic['Q4'] += 1

for i in dic:
    print(f'{i}: {dic[i]}')
