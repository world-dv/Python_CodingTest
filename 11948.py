arr = []
for _ in range(4):
    arr.append(int(input()))
a = sum(sorted(arr)[1:])

e = int(input())
f = int(input())
print(a + max(e, f))
