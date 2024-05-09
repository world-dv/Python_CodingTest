import sys
import math
n, k = map(int, sys.stdin.readline().rstrip().split())
student_man = [0 for _ in range(6)]
student_woman = [0 for _ in range(6)]
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if x:
        student_man[y-1] += 1
    else:
        student_woman[y-1] += 1
answer = 0
for i in range(6):
    answer += math.ceil(student_man[i] / k)
    answer += math.ceil(student_woman[i] / k)
print(answer)
