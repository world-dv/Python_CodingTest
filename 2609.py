from math import gcd
a, b = map(int, input().split())

x = gcd(a, b)
y = a * b // x
print(x)
print(y)
