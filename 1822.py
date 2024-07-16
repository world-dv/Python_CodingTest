nA, nB = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(f'{len(a - b)}\n{" ".join(map(str, sorted(a - b)))}')
