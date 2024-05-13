import sys
n = 4

arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

answer = []
for i in range(n):
    x1, y1, p1, q1, x2, y2, p2, q2 = arr[i]
    if p1 < x2 or p2 < x1 or q2 < y1 or q1 < y2:
        answer.append('d')
    elif [x1, y1] == [p2, q2] or [x1, q1] == [p2, y2] or [p1, y1] == [x2, q2] or [p1, q1] == [x2, y2]:
        answer.append('c')
    elif x1 == p2 or x2 == p1 or q1 == y2 or y1 == q2:
        answer.append('b')
    else:
        answer.append('a')
print('\n'.join(answer))
