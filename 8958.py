n = int(input())

quiz = []
for i in range(n):
    quiz.append(input())

for i in range(n):
    answer = 0
    end = 0
    for q in quiz[i]:
        if not end and q == 'O':
            end = 1
        elif q == 'O':
            end = end + 1
        else:
            end = 0
        answer += end
    print(answer)
