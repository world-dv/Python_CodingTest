total = 0
max_total = 0
for _ in range(10):
    off, on = map(int, input().split())
    total += on - off
    max_total = max(total, max_total)
print(max_total)
