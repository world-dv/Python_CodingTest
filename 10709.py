import sys
h, w = map(int, sys.stdin.readline().split())
cloud = []
for _ in range(h):
    cloud.append(list(sys.stdin.readline()))

answer = []
for i in range(h):
    stack = []
    for j in range(w):
        if cloud[i][j] == 'c':
            stack.append(0)
        elif stack and cloud[i][j] == '.' and stack[-1] != -1:
            stack.append(stack[-1] + 1)
        else:
            stack.append(-1)
    answer.append(stack)

for i in answer:
    print(' '.join(map(str, i)))
