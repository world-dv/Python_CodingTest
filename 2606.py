from collections import defaultdict, deque
n = int(input())
m = int(input())

dic = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

visit = [0 for _ in range(n+1)]
q = deque()
q.append(1)
while q:
    x = q.popleft()
    visit[x] = 1

    for i in dic[x]:
        if not visit[i]:
            q.append(i)

print(sum(visit) - 1)
