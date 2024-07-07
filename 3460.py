t = int(input())
for _ in range(t):
    x = int(input())
    x = bin(x)[:1:-1]
    answer = []
    for i in range(len(x)):
        if x[i] == '1':
            answer.append(str(i))
    print(' '.join(answer))
