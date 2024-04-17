n = int(input())

line = 1
while n > line:
    n -= line
    line += 1

a, b = 0, 0
if line % 2 != 0:
    a = line - n + 1
    b = n
else:
    a = n
    b = line - n + 1
print(f'{a}/{b}')
