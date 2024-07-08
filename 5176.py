k = int(input())
for _ in range(k):
    arr = []
    answer = 0
    p, m = map(int, input().split())
    for _ in range(p):
        x = int(input())
        if x in arr:
            answer += 1
        else:
            arr.append(x)
    print(answer)
