N, B = map(int, input().split())
n_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = ''
while N > 0:
    answer += n_list[N % B]
    N //= B
print(answer[::-1])
