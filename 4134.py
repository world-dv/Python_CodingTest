import sys
N = int(sys.stdin.readline().rstrip())


def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for _ in range(N):
    a = int(sys.stdin.readline().rstrip())
    while True:
        if prime(a):
            break
        a += 1
    print(a)
