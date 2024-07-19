a, b, n = map(int, input().split())
a %= b
cnt = 0
x = 0
while cnt < n:
    x = a * 10 // b
    a = a * 10 % b
    cnt += 1
print(x)
