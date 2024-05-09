import sys
square = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            if not square[i][j]:
                square[i][j] = 1

answer = 0
for i in square:
    answer += sum(i)
print(answer)
