n = int(input())
student = list(map(int, input().split()))
line = [i for i in range(1, n+1)]

for i in range(n):
    if student[i] == 0:
        continue
    else:
        line.remove(i+1)
        line.insert(i - student[i], i+1)
print(' '.join(map(str, line)))
