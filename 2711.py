t = int(input())
for _ in range(t):
    pos, words = input().split()
    pos = int(pos)
    words = words[:pos-1] + words[pos:]
    print(words)
