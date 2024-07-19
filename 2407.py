import math
n, m = map(int, input().split())
total = 1
tmp = m
for i in range(n, n - tmp, -1):
    total *= i
print(total // math.factorial(m))
