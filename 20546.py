money = int(input())
arr = list(map(int, input().split()))

jh = [money, 0]
sm = [money, 0]
cnt_up = 0
cnt_down = 0
up = down = arr[0]
for idx, i in enumerate(arr):
    if sm[0] >= i:
        a = sm[0] // i
        sm[1] += sm[0] // i
        sm[0] -= i * a
    if up < i:
        cnt_up += 1
        cnt_down = 0
    if down > i:
        cnt_down += 1
        cnt_up = 0
    if cnt_up == 3:
        cnt_up = 0
        jh[0] += jh[1] * i
        jh[1] = 0
    if cnt_down == 3 and jh[0] >= i:
        cnt_down -= 1
        a = jh[0] // i
        jh[1] += jh[0] // i
        jh[0] -= i * a
    up = down = i

if jh[0] + jh[1] * arr[-1] > sm[0] + sm[1] * arr[-1]:
    print('TIMING')
elif jh[0] + jh[1] * arr[-1] < sm[0] + sm[1] * arr[-1]:
    print('BNP')
else:
    print('SAMESAME')
