N = int(input())
arr = list(map(int, input().split()))
start = 1
stack = []
while arr:
    a = arr.pop(0)
    if a == start:
        start += 1
    else:
        stack.append(a)
    while stack and stack[-1] == start:
        stack.pop()
        start += 1

if len(stack) == 0:
    print('Nice')
else:
    print('Sad')
