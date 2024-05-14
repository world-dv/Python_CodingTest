import sys

move = {'R': 0, 'L': 1, 'B': 2, 'T': 3, 'RT': 4, 'LT': 5, 'RB': 6, 'LB': 7}
dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

king, stone, n = sys.stdin.readline().rstrip().split()
command = [move[sys.stdin.readline().rstrip()] for _ in range(int(n))]

king_x = 8 - int(king[1])
king_y = ord(king[0]) - ord('A')

stone_x = 8 - int(stone[1])
stone_y = ord(stone[0]) - ord('A')

for i in command:
    nx, ny = king_x + dx[i], king_y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        if nx == stone_x and ny == stone_y:
            sx, sy = stone_x + dx[i], stone_y + dy[i]
            if 0 <= sx < 8 and 0 <= sy < 8:
                stone_x, stone_y = sx, sy
                king_x, king_y = nx, ny
        else:
            king_x, king_y = nx, ny
print(f'{chr(65 + king_y)}{8 - king_x}')
print(f'{chr(65 + stone_y)}{8 - stone_x}')
