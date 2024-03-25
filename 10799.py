arr = input()
answer = 0
stack = []
for i, j in enumerate(arr):
    if j == '(':
        stack.append('(')
    else:
        stack.pop()
        if arr[i-1] == '(':
            answer += len(stack)
        else:
            answer += 1
print(answer)
