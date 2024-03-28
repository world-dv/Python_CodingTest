from collections import deque
import sys
N = int(input())
q = deque(enumerate(map(int, sys.stdin.readline().split())))
answer = []

while q:
    idx, a = q.popleft()
    answer.append(idx+1)

    if a > 0:
        q.rotate(-(a-1))
    elif a < 0:
        q.rotate(-a)
print(' '.join(map(str, answer)))
