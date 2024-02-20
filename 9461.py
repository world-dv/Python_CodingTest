T = int(input())
N = []
for i in range(T):
    N.append(int(input()))

P = [0 for _ in range(max(N)+1)]
P[0], P[1], P[2] = 1, 1, 1
for i in range(3, len(P)):
    P[i] = P[i-2] + P[i-3]

for i in N:
    print(P[i-1])
