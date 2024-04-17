N = int(input())

answer = [1, 1]
for i in range(2, N):
    answer.append(answer[i-2] + answer[i-1])
print(answer[N-1])
