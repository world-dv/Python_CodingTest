import sys
w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(sys.stdin.readline())

x = (p + t) % w if ((p + t) // w) % 2 == 0 else w - (p + t) % w
y = (q + t) % h if ((q + t) // h) % 2 == 0 else h - (q + t) % h
print(x, y)
