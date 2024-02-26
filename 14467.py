N = int(input())
dic = dict()

for i in range(N):
    a, b = map(int, input().split())

    if a not in dic:
        dic[a] = [b, 0]
    else:
        if dic[a][0] != b:
            dic[a][0] = b
            dic[a][1] += 1

answer = 0
for i in dic:
    answer += dic[i][1]
print(answer)
