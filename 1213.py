import sys
from collections import Counter
n = sys.stdin.readline().rstrip()
a = Counter(n)
b = sorted(set(n))

answer = ''
for i in b:
    answer += i * (a[i] // 2)
    a[i] = a[i] % 2
    if a[i] == 0:
        del a[i]

if len(a) > 1:
    answer = "I'm Sorry Hansoo"
else:
    answer2 = answer[::-1]
    if len(a) == 1:
        for i in b:
            if i in a and a[i] == 1:
                answer += i
                break
    answer = answer + answer2
print(answer)
