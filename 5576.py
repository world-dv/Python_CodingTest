w = [int(input()) for _ in range(10)]
k = [int(input()) for _ in range(10)]
w = sorted(w, reverse=True)
k = sorted(k, reverse=True)
print(f'{sum(w[:3])} {sum(k[:3])}')
