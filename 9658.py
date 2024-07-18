n = int(input())
turn = [1, 1, 0, 1, 0]
for i in range(5, n+1):
    if turn[i - 1] + turn[i - 3] + turn[i - 4] == 0:
        turn.append(1)
    else:
        turn.append(0)
print('CY' if turn[n] else 'SK')
