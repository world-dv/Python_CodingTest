n, m = map(int, input().split())
j = int(input())
start = 1
end = m
total = 0
for _ in range(j):
    apple = int(input())
    if start <= apple <= end:
        continue
    elif start > apple:
        end -= (start - apple)
        total += (start - apple)
        start = apple
    else:
        start += (apple - end)
        total += (apple - end)
        end = apple
print(total)
