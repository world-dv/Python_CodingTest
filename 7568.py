n = int(input())
people = []
for _ in range(n):
    people.append(list(map(int, input().split())))

ranking = [1] * n
for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j and people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            cnt += 1
    ranking[i] += cnt
print(' '.join(map(str, ranking)))

