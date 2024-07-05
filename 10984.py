t = int(input())

for _ in range(t):
    n = int(input())
    total, gpa = 0, 0
    for _ in range(n):
        c, g = map(float, input().split())
        total += c
        gpa += g * c
    print(f'{int(total)} {round(gpa / total,1)}')
