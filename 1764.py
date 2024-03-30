N, M = map(int, input().split())
s = set()
for _ in range(N):
    s.add(input())

answer = set()
for _ in range(M):
    x = input()
    if x in s:
        answer.add(x)

print(len(answer))
print('\n'.join(sorted(answer)))
