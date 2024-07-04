n = int(input())
total = 0
for _ in range(n):
    s, a = map(int, input().split())
    total += a % s
print(total)
