import sys
n = int(sys.stdin.readline())
switch = [0] + list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    if x == 1:
        for i in range(1, n // y + 1):
            switch[i * y] = 0 if switch[i * y] == 1 else 1
    else:
        start = y - 1
        end = y + 1
        switch[y] = 0 if switch[y] == 1 else 1
        while 0 < start < end <= n:
            if switch[start] == switch[end]:
                switch[start] = 0 if switch[start] == 1 else 1
                switch[end] = 0 if switch[end] == 1 else 1
                start -= 1
                end += 1
            else:
                break
for i in range(1, n+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
