bingo = [list(map(int, input().split())) for _ in range(5)]


def color(ar, n):
    for i in range(5):
        for j in range(5):
            if ar[i][j] == n:
                ar[i][j] = 0
                return ar
    return ar


def speakBingo(ar):
    check = 0
    b, c = 0, 0
    for i in range(5):
        b += ar[i][i]
        c += ar[i][4-i]
        a = 0
        for j in range(5):
            a += ar[j][i]
        check += int(a == 0)
        check += int(sum(ar[i]) == 0)
    check += int(b == 0)
    check += int(c == 0)
    return check >= 3


answer = 0
k = 0
for i in range(5):
    arr = list(map(int, input().split()))
    speak = 0
    for x in arr:
        answer += 1
        bingo = color(bingo, x)
        if speakBingo(bingo):
            k = x
            break
    if k != 0:
        break
print(answer)
