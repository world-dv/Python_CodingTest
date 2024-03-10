L, P = map(int, input().split())
L_Number = list(map(int, input().split()))
L_Number = list(map(lambda x: x - L * P, L_Number))
for i in L_Number:
    print(i, end=' ')
