import os
import random
import time

from curses import wrapper

pacman_sprite = "󰮯 "
wall = "██"
space = "  "
goal = "▓▓"

vec_sum = lambda v1, v2: [num+v2[idx] for idx, num in enumerate(v1)]
gather  = lambda v, indices: [v[i] for i in indices]
def main(stdscr):
    # Clear screen
    stdscr.clear()

    m = genarate_maze()
    for i in m:
        stdscr.addstr(0, 0, f'{i}')
        stdscr.refresh()
        time.sleep(10)

    stdscr.getkey()

# def main(stdscr):
    # stdscr.clear()
    # stdscr.refresh()
    # count = 0
    # m = genarate_maze()
    # while True:
    #     maze_ = next(m)
    #     stdscr.addstr(0, 0, maze_)
    #     stdscr.refresh()
    #     stdscr.clear()
    #     time.sleep(0.01)
    #     count += 1
    #     if count % 60 == 0:
    #         stdscr.clear()
    #     stdscr.getkey()
    # pass

def genarate_maze():
    size = 40
    maze = [[1 for j in range(size)] for i in range(size)]
    pacman = [0, 1]
    path = []
    count = 0
    maze[size-2][size-2] = -1
    while pacman != [size-2, size-2] or count < size^2:
        count += 1
        maze[pacman[0]][pacman[1]] = 0

        moves = {
            "up": [0, -1],
            "down": [0, 1],
            "right": [1, 0],
            "left": [-1, 0],
        }

        if pacman[0] <= 1:
            moves.pop("left")
        if pacman[0] >= size-2:
            moves.pop("right")
        if pacman[1] <= 1:
            moves.pop("up")
        if pacman[1] >= size-2:
            moves.pop("down")

        for k, m in moves.copy().items():
            if maze[pacman[0]+m[0]*2][pacman[1]+m[1]*2] == 0:
                moves.pop(k)

        if moves:
            path.append(pacman) 
            move = random.choice(list(moves.values()))
            pacman = [coor+move[idx]*2 for idx, coor in enumerate(pacman)]
            mid = [coor+move[idx] for idx, coor in enumerate(pacman)]
            maze[pacman[0]][pacman[1]] = 2
            maze[mid[0]][mid[1]] = 0
        else:
            pacman = path.pop()

        def match_arr(x:int):
            match x:
                case 1: return wall
                case 0: return space
                case -1: return goal
                case 2: return pacman_sprite
                case _: raise ValueError(f"not found element {x}")

        m = '\n'.join(
            ''.join(
                map(match_arr, row)
            ) for row in maze
        )

        yield m

m = genarate_maze()
for i in m:
    print(i)
    # time.sleep(.1)
    os.system('clear')

# wrapper(main)

