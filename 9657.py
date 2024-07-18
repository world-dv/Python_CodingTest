n = int(input())
turn = [1, 1, 0, 1, 1]
for i in range(5, n+1):
    if turn[i-1] + turn[i-3] + turn[i-4] == 3:
        turn.append(0)
    else:
        turn.append(1)
print('SK' if turn[n] else 'CY')
