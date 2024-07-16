x = int(input())
sticks = [64]

while True:
    if sum(sticks) == x:
        break
    a = sticks.pop(sticks.index(min(sticks)))
    if sum(sticks) + a // 2 < x:
        sticks.append(a // 2)
    sticks.append(a // 2)
print(len(sticks))
