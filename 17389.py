import sys
N = int(sys.stdin.readline())
XO = sys.stdin.readline().rstrip()
bonus, answer = 0, 0
for i, j in enumerate(XO):
    if j == 'X':
        bonus = 0
    else:
        answer += (i+1) + bonus
        bonus += 1
print(answer)
