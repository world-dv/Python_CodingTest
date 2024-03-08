from functools import cmp_to_key
N = int(input())

arr = set()
for i in range(N):
    arr.add(input())


def calculate(a, b):
    if len(a) == len(b):
        return int(b < a) - int(a < b)
    else:
        return int(len(a) > len(b)) - int(len(a) < len(b))


arr = sorted(arr, key=cmp_to_key(calculate))

for i in arr:
    print(i)
