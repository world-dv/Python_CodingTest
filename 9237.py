n = int(input())
tree = list(map(int, input().split()))
tree = sorted(tree, reverse=True)
total = 0
for i in range(n):
    total = max(total, i + tree[i])
print(total + 2)
