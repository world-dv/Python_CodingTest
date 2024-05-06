import sys
n = int(sys.stdin.readline().rstrip())

white = 0
blue = 0


def checkSquare(graph, x, y, k):
    global white, blue
    total = 0
    for i in range(x, x+k):
        total += sum(graph[i][y:y+k])
    if total == 0:
        white += 1
        return
    elif total == k ** 2:
        blue += 1
        return
    else:
        k //= 2
        checkSquare(graph, x, y, k)
        checkSquare(graph, x + k, y, k)
        checkSquare(graph, x, y + k, k)
        checkSquare(graph, x + k, y + k, k)


paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

checkSquare(paper, 0, 0, n)
print(white)
print(blue)
