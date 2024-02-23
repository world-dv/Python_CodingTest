from math import ceil
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for i in A:
    i -= B
    sub = 0 if i <= 0 else ceil(i / C)
    answer += 1 + sub
print(answer)
