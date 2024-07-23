n = int(input())
graph = []
for _ in range(n):
    graph.append(list('.' * n))
command = list(input())
move_x = {'U': -1, 'D': 1, 'R': 0, 'L': 0}
move_y = {'U': 0, 'D': 0, 'R': 1, 'L': -1}
start_x, start_y = 0, 0
for i in command:
    next_x, next_y = start_x + move_x[i], start_y + move_y[i]
    if 0 <= next_x < n and 0 <= next_y < n:
        if i == 'U' or i == 'D':
            if graph[start_x][start_y] == '-':
                graph[start_x][start_y] = '+'
            elif graph[start_x][start_y] == '.':
                graph[start_x][start_y] = '|'
            start_x = next_x
            start_y = next_y
            if graph[start_x][start_y] == '-':
                graph[start_x][start_y] = '+'
            elif graph[start_x][start_y] == '.':
                graph[start_x][start_y] = '|'
        else:
            if graph[start_x][start_y] == '|':
                graph[start_x][start_y] = '+'
            elif graph[start_x][start_y] == '.':
                graph[start_x][start_y] = '-'
            start_x = next_x
            start_y = next_y
            if graph[start_x][start_y] == '|':
                graph[start_x][start_y] = '+'
            elif graph[start_x][start_y] == '.':
                graph[start_x][start_y] = '-'
for x in graph:
    print(''.join(x))
