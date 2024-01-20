import random

pacman_sprite = "󰮯 "
wall_ = "██"
space = "  "
goal = "▓▓"

size = 48
maze = [[0 for j in range(size)] for i in range(size)]

for b in range(size):
    maze[b][0] = maze[b][size-1] = 1
    maze[0][b] = maze[size-1][b] = 1

for i in range(2, size-2):
    for j in range(2, size-2):
        if i % 2 or j % 2: continue
        maze[i][j] = 1

        moves = {
            "up": [0, -1],
            "down": [0, 1],
            "right": [1, 0],
            "left": [-1, 0],
        }

        if i <= 1:
            moves.pop("left")
        if i >= size-2:
            moves.pop("right")
        if j <= 1:
            moves.pop("up")
        if j >= size-2:
            moves.pop("down")

        move = random.choice(list(moves.values()))
        wall = [coor+move[idx] for idx, coor in enumerate([i, j])]
        maze[wall[0]][wall[1]] = 1



def match_arr(x:int):
    match x:
        case 1: return wall_
        case 0: return space
        case -1: return goal
        case 2: return pacman_sprite
        case _: raise ValueError(f"not found element {x}")

m = '\n'.join(
    ''.join(map(match_arr, row))
    for row in maze
)
print(m)
