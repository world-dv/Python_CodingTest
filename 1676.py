import math
n = int(input())
m = str(math.factorial(n))[::-1]
cnt = 0
for i in m:
    if i != '0':
        break
    cnt += 1
print(cnt)
