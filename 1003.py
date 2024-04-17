n = int(input())

dp_0 = [1, 0]
dp_1 = [0, 1]

for i in range(2, 41):
    dp_0.append(dp_0[i-2] + dp_0[i-1])
    dp_1.append(dp_1[i-2] + dp_1[i-1])

for _ in range(n):
    m = int(input())
    print(dp_0[m], dp_1[m])
