score = []
for i in range(8):
    score.append([int(input()), i+1])
score = sorted(score, key=lambda x: -x[0])
arr = sorted(score[:5], key=lambda x: x[1])
total = 0
answer = []
for i in arr:
    total += i[0]
    answer.append(str(i[1]))
print(f'{total}\n{" ".join(answer)}')
