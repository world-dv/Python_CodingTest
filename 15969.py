import sys
N = int(sys.stdin.readline().rstrip())
score = set(map(int, sys.stdin.readline().rstrip().split()))
print(max(score) - min(score))
