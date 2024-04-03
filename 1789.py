S = int(input())
cnt = 0
for i in range(1, S+1):
    if S >= i:
        S -= i
    else:
        break
    cnt += 1
print(cnt)
