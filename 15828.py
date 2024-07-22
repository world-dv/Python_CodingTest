from collections import deque
import sys
n = int(sys.stdin.readline())
stack = deque()
while True:
    x = int(sys.stdin.readline())
    if x == -1:
        break
    if x == 0:
        stack.popleft()
    elif len(stack) < n:
        stack.append(x)
if stack:
    print(*stack)
else:
    print('empty')
