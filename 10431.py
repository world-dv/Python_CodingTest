import sys
n = int(sys.stdin.readline())

for _ in range(n):
    student = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for i in range(1, 20):
        for j in range(i+1, 21):
            if student[i] > student[j]:
                student[i], student[j] = student[j], student[i]
                cnt += 1
    print(student[0], cnt)

