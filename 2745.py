N, B = input().split()
n_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = 0
n = len(N) - 1
for i in range(len(N)):
    answer += n_list.index(N[i]) * (int(B) ** (n - i))
print(answer)
