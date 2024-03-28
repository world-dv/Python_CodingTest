import sys
N = sys.stdin.readline().rstrip()
N = sorted(N, reverse=True)
print(''.join(N))
