e, s, m = map(int, input().split())
total = 1
while True:
    if (total - e) % 15 == 0 and (total - s) % 28 == 0 and (total - m) % 19 == 0:
        break
    total += 1
print(total)
