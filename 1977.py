m = int(input())
n = int(input())

total = 0
min_answer = n
for i in range(m, n+1):
    if int(i ** 0.5) ** 2 == i:
        total += i
        min_answer = min(i, min_answer)
if total == 0:
    print(-1)
else:
    print(f'{total}\n{min_answer}')
