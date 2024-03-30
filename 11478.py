s = input()
answer = set()
for i in range(1, len(s)):
    for a in range(len(s)):
        answer.add(s[a:a+i])
print(len(answer) + 1)
