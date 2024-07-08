s = input()
answer = ""
for i in range(len(s)):
    if s[i].isalpha():
        x = ord(s[i]) + 13
        if s[i].islower():
            if x > ord('z'):
                x = ord('a') + x - ord('z') - 1
        else:
            if x > ord('Z'):
                x = ord('A') + x - ord('Z') - 1
        answer += (chr(x))
    else:
        answer += s[i]
print(answer)
