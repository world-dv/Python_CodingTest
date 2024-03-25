import sys
N = int(input())
stack = []
for _ in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 3:
        print(len(stack))
    elif command[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[-1])
