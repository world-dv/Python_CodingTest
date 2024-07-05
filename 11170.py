n = int(input())
for _ in range(n):
    start, end = map(int, input().split())
    cnt = 0
    for i in range(start, end+1):
        cnt += str(i).count('0')
    print(cnt)
