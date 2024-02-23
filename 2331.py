from collections import Counter
A, P = map(int, input().split())

D = [0 for _ in range(10000)]
D[0] = A


def calculate(x):
    n = 0
    while x > 0:
        a = x % 10
        n += (a ** P)
        x //= 10
    return n


for i in range(1, 10000):
    D[i] = calculate(D[i-1])


d = Counter(D)
answer = 0
for i in d:
    if d[i] == 1:
        answer += 1
print(answer)
