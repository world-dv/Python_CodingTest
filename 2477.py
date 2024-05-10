import sys
k = int(sys.stdin.readline())

number = []
square = []
for _ in range(6):
    x, y = map(int, sys.stdin.readline().split())
    number.append(x)
    square.append(y)

long = 0
short = 0
for i in range(6):
    if number.count(number[i]) == 1:
        if not long:
            long = square[i]
        else:
            long *= square[i]
        min_idx = (i + 3) % 6
        if not short:
            short = square[min_idx]
        else:
            short *= square[min_idx]

print((long - short) * k)
