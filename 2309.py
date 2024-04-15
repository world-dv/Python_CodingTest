from itertools import permutations
tall = []
for i in range(9):
    tall.append(int(input()))
tall.sort()

target = []
total = permutations(tall, 7)
for i in total:
    if sum(i) == 100:
        target = i
        break
for i in target:
    print(i)
