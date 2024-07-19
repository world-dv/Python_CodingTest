n = int(input())
m = 0
change = 100001
while True:
    if n < 5 * m:
        break
    a = n - 5 * m
    if a % 2 == 0:
        change = min(change, m + a // 2)
    m += 1
if change == 100001:
    change = -1
print(change)
