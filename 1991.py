import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())

graph = defaultdict(list)
for i in range(n):
    root, left, right = sys.stdin.readline().split()
    graph[root] = [left, right]


# 전위
def preorder(r):
    if r != '.':
        print(r, end='')
        preorder(graph[r][0])
        preorder(graph[r][1])


# 중위
def inorder(r):
    if r != '.':
        inorder(graph[r][0])
        print(r, end='')
        inorder(graph[r][1])


# 후위
def postorder(r):
    if r != '.':
        postorder(graph[r][0])
        postorder(graph[r][1])
        print(r, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
