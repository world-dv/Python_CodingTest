N = int(input())
answer = 0
for _ in range(N):
    arr = input()
    stack = []
    for i in arr:
        if not stack or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()
    answer += 1 if len(stack) == 0 else 0
print(answer)
