n = int(input())
turn = n // 3 + n % 3
print('SK' if turn % 2 != 0 else 'CY')
