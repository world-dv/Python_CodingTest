st = list(input())

answer = []
stack = []
check = 0
for s in st:
    if s == '<':
        check = 1
    if s == '<' or s == ' ':
        while stack:
            answer.append(stack.pop())
        answer.append(s)
    elif s == '>':
        check = 0
        answer.append(s)
    else:
        if check:
            answer.append(s)
        else:
            stack.append(s)
while stack:
    answer.append(stack.pop())
print(''.join(answer))

