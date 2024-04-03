plate = input()
answer = 10
for i in range(1, len(plate)):
    if plate[i-1] != plate[i]:
        answer += 10
    else:
        answer += 5
print(answer)
