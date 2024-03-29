from math import gcd
aa, ab = map(int, input().split())
ba, bb = map(int, input().split())

c = (ab * bb) // gcd(ab, bb)
ca = aa * (c // ab) + ba * (c // bb)
x = gcd(c, ca)
print(ca // x, c // x)
