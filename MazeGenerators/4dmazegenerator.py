import random
# if your computer or device can't run colorama, just delete these two lines and remove "FORE.<color>" in print_maze.
from colorama import init, Fore
init()

# this text controls what you see. Default is 'C', '#', 'U', 'D', 'F', 'B'.
cell = 'C'
wall = '#'
up = 'U'
down = 'D'
forward = 'F'
backward = 'B'

# these control how big your maze is. Change them to what you want.
# 4x4x1x1 is the smallest you can go with it.
length = 10
width = 10
depth = 10
space = 10


# 4d coordinate logic is similar to both the previous 3d and 2d coordinate logic, however a bit more insanely.
# due to "space" being added, the coordinates are now (w, z, y, x) and space starts at the first object to the last.
def make_4d_maze(ln, wd, dp, sp):
    """Creates maze by making a quadruple nested loop with all the characters being walls."""
    maze = []  # the list that will hold the maze.
    for w in range(0, sp):
        volume = []  # a volume holds a collection of boards that make up a 3d object.
        for z in range(0, dp):  # keep making boards of lines for how much the depth is.
            board = []  # a board stores a series of lines.
            for y in range(0, wd):  # keep making lines of characters for how much width there is.
                line = []  # a line stores lists that contain characters.
                for x in range(0, ln):  # keep making characters for how much length there is.
                    line.append(wall)  # appends a wall to the list.
                board.append(line)  # appends the list to the board once all of the walls have been appended.
            volume.append(board)  # appends the board to a volume once all of the lines have been appended.
        maze.append(volume)  # appends the volume to the board once all of the boards have been appended.
    return maze  # once finished, return the maze.


def print_maze(maze, ln, wd, dp, sp):
    """Prints the maze with colors (or not) in an organized and easy to read way."""
    for w in range(0, sp):  # for as many objects as there are in the maze
        print(Fore.RESET, f"\n Object {w+1}:\n")
        for z in range(0, dp):  # for as many boards as there are in the object
            for y in range(0, wd):  # for as many lines as there are in the board
                for x in range(0, ln):  # for as many characters are there in the line
                    if maze[w][z][y][x] == cell:  # if the character is a cell, make it green.
                        print(Fore.GREEN, f'{maze[w][z][y][x]}', end="")
                    elif maze[w][z][y][x] == wall:  # if the character is a wall, make it red.
                        print(Fore.RED, f'{maze[w][z][y][x]}', end="")
                    elif maze[w][z][y][x] == up:  # if the character is an up, make it blue.
                        print(Fore.BLUE, f'{maze[w][z][y][x]}', end="")
                    elif maze[w][z][y][x] == down:  # if the character is a down, make it yellow.
                        print(Fore.YELLOW, f'{maze[w][z][y][x]}', end="")
                    elif maze[w][z][y][x] == forward:  # if the character is a forward, make it "magenta".
                        print(Fore.MAGENTA, f'{maze[w][z][y][x]}', end="")
                    elif maze[w][z][y][x] == backward:  # if the character is a backward, make it cyan.
                        print(Fore.CYAN, f'{maze[w][z][y][x]}', end="")
                    else:  # if an incorrect or invalid letter is printed, make it "white".
                        print(Fore.WHITE, f'{maze[w][z][y][x]}', end="")
                print('')
            print('\n')


# create the maze based on the length, width, depth and space specified.
the_maze = make_4d_maze(length, width, depth, space)
# I'm sorry if it hurts you that all the following code below is not in a def function. I made it to be simple.

starting_w = random.randint(0, space-1)  # makes a random w-coordinate
starting_z = random.randint(0, depth-1)  # makes a random z-coordinate
starting_y = random.randint(0, width-1)  # makes a random y-coordinate
starting_x = random.randint(0, length-1)  # makes a random x-coordinate

# here, we make sure that the starting coordinate cell isn't going to clip into a wall.
# if you're wondering why it's -2 on some of them instead of just -1, it's just to be safe on the bug side.
if starting_x == 0:  # if starting_x is on the edge, change the position.
    starting_x += 2
if starting_x == 1:
    starting_x += 1
if starting_x == length - 1:  # vice versa.
    starting_x -= 2
if starting_x == length - 2:
    starting_x -= 1
if starting_y == 0:  # if starting_y is on the edge, change the position.
    starting_y += 2
if starting_y == 1:
    starting_y += 1
if starting_y == width - 1:  # vice versa.
    starting_y -= 2
if starting_y == width - 2:
    starting_y -= 1

# make the random start position in the maze a cell.
the_maze[starting_w][starting_z][starting_y][starting_x] = cell

# add in the walls that are around the beginning cell to begin the fun.
walls = [[starting_w, starting_z, starting_y - 1, starting_x], [starting_w, starting_z, starting_y, starting_x - 1],
         [starting_w, starting_z, starting_y, starting_x + 1], [starting_w, starting_z, starting_y + 1, starting_x],
         [starting_w, starting_z - 1, starting_y, starting_x], [starting_w, starting_z + 1, starting_y, starting_z],
         [starting_w - 1, starting_z, starting_y, starting_x], [starting_w + 1, starting_z, starting_y, starting_x]]

while len(walls) > 0:  # while there are still walls in the walls list. Yes, it does have to be len(walls).
    rando_choice = random.randint(0, len(walls) - 1)  # gets a random index to choose from
    random_wall = walls[rando_choice]  # uses that random index to get a random wall from the walls list.
    if random_wall[0] < 0 or random_wall[0] > space - 1:  # if the wall is out of bounds, remove and start again.
        del walls[rando_choice]
        continue
    if random_wall[1] < 0 or random_wall[1] > depth - 1:
        del walls[rando_choice]
        continue
    if random_wall[2] < 1 or random_wall[2] > width - 2:
        del walls[rando_choice]
        continue
    if random_wall[3] < 1 or random_wall[3] > length - 2:
        del walls[rando_choice]
        continue
    if the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3]] != wall:  # if the "wall" isn't a wall, remove.
        del walls[rando_choice]
        continue

    # keeps track of how many cells are nearby the wall. In dimensions of 3 and higher, it has to be ONLY 1.
    # if the cell count is 1, that wall turns into a cell or other equivalent. If lower or higher, forget and remove.
    cell_count = 0
    if random_wall[0] - 1 < 0:  # if the random wall's neighbor is out of bounds, don't check if it's a cell.
        cell_count = cell_count  # random code to do something other than nothing or something bad
    elif the_maze[random_wall[0] - 1][random_wall[1]][random_wall[2]][random_wall[3]] != wall:  # if the neighbor isn't a wall, increment cell count.
        cell_count += 1

    if random_wall[0] + 1 > space - 1:
        cell_count = cell_count
    elif the_maze[random_wall[0] + 1][random_wall[1]][random_wall[2]][random_wall[3]] != wall:
        cell_count += 1

    if random_wall[1] - 1 < 0:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1] - 1][random_wall[2]][random_wall[3]] != wall:
        cell_count += 1

    if random_wall[1] + 1 > depth - 1:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1] + 1][random_wall[2]][random_wall[3]] != wall:
        cell_count += 1

    if random_wall[2] - 1 < 0:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1]][random_wall[2] - 1][random_wall[3]] != wall:
        cell_count += 1

    if random_wall[2] + 1 > width - 1:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1]][random_wall[2] + 1][random_wall[3]] != wall:
        cell_count += 1

    if random_wall[3] - 1 < 0:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3] - 1] != wall:
        cell_count += 1

    if random_wall[3] + 1 > length - 1:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3] + 1] != wall:
        cell_count += 1

    if cell_count == 1:  # if the wall passed the skill check, determine where the one cell it came from was at.
        while True:  # this loop is used primarily to catch bugs, but is also just a nice safety net in general.
            if random_wall[0] - 1 < 0:
                cell_count = cell_count
                # note that "is a cell" down below really means "isn't a wall"
            elif the_maze[random_wall[0] - 1][random_wall[1]][random_wall[2]][random_wall[3]] != wall:  # if the block backward is a cell,
                the_maze[random_wall[0] - 1][random_wall[1]][random_wall[2]][random_wall[3]] = forward  # make it a forward
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3]] = backward  # make the current block a backward.
                break

            if random_wall[0] + 1 > space - 1:
                cell_count = cell_count
            elif the_maze[random_wall[0] + 1][random_wall[1]][random_wall[2]][random_wall[3]] != wall:  # if the block forward is a cell,
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3]] = backward  # make it a backward
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3]] = forward  # make the current block a forward.
                break

            if random_wall[1] - 1 < 0:
                cell_count = cell_count
            elif the_maze[random_wall[0]][random_wall[1] - 1][random_wall[2]][random_wall[3]] != wall:  # if the block above is a cell,
                the_maze[random_wall[0]][random_wall[1] - 1][random_wall[2]][random_wall[3]] = down  # make it a down
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3]] = up  # make the current block an up.
                break

            if random_wall[1] + 1 > depth - 1:
                cell_count = cell_count
            elif the_maze[random_wall[0]][random_wall[1] + 1][random_wall[2]][random_wall[3]] != wall:  # if the block below is a cell,
                the_maze[random_wall[0]][random_wall[1] + 1][random_wall[2]][random_wall[3]] = up  # make it an up
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3]] = down  # make the current block a down.
                break

            if random_wall[2] - 1 < 0:
                cell_count = cell_count
            elif the_maze[random_wall[0]][random_wall[1]][random_wall[2] - 1][random_wall[3]] != wall:  # if the block north is a cell,
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3]] = cell  # make the current block a cell.
                break

            if random_wall[2] + 1 > width - 1:
                cell_count = cell_count
            elif the_maze[random_wall[0]][random_wall[1]][random_wall[2] + 1][random_wall[3]] != wall:  # if the block south is a cell,
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3]] = cell  # make the current block a cell.
                break

            if random_wall[3] - 1 < 0:
                cell_count = cell_count
            elif the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3] - 1] != wall:  # if the block west is a cell,
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3]] = cell  # make the current block a cell.
                break

            if random_wall[3] + 1 > length - 1:
                cell_count = cell_count
            elif the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3] + 1] != wall:  # if the block east is a cell,
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]][random_wall[3]] = cell  # make the current block a cell.
                break

        # attempt to add all neighboring walls, including ones above, below, infront of and behind the cell.
        try:
            walls.append([random_wall[0] - 1, random_wall[1], random_wall[2], random_wall[3]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0] + 1, random_wall[1], random_wall[2], random_wall[3]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1] - 1, random_wall[2], random_wall[3]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1] + 1, random_wall[2], random_wall[3]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1], random_wall[2] - 1, random_wall[3]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1], random_wall[2] + 1, random_wall[3]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1], random_wall[2], random_wall[3] - 1])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1], random_wall[2], random_wall[3] + 1])
        except IndexError:
            pass

        del walls[rando_choice]  # once done with adding neighboring walls, delete itself in the walls list
    else:  # if the wall had 2 or more cells nearby, delete itself in the walls list and go back to the start
        del walls[rando_choice]

# don't change any of these values. they function on their own.
# these values make sure that an entrance and an exit to the maze are made.
# explanation for how this works can be found in the 2d maze generator. This is similar, but goes in three directions.
a = 0
b = 0
c = 1
d = 1
the_maze[a][b][c - 1][d] = cell
constant = 1
while True:
    if constant == 1:
        if the_maze[a][b][c][d] == wall:
            the_maze[a][b][c][d] = cell
        else:
            break
    d += constant
    if the_maze[a][b][c][d] == wall:
        the_maze[a][b][c][d] = cell
    else:
        break
    d -= constant
    c += constant
    if the_maze[a][b][c][d] == wall:
        the_maze[a][b][c][d] = cell
    else:
        break
    c -= constant
    b += constant
    if the_maze[a][b][c][d] == wall:
        the_maze[a][b][c][d] = down
        the_maze[a][b - 1][c][d] = up
    else:
        break
    b -= constant
    constant += 1

e = space - 1
f = depth - 1
g = width - 2
h = length - 2
the_maze[e][f][g + 1][h] = cell
constant = 1
while True:
    if constant == 1:
        if the_maze[e][f][g][h] == wall:
            the_maze[e][f][g][h] = cell
        else:
            break
    g -= constant
    if the_maze[e][f][g][h] == wall:
        the_maze[e][f][g][h] = cell
    else:
        break
    g += constant
    h -= constant
    if the_maze[e][f][g][h] == wall:
        the_maze[e][f][g][h] = cell
    else:
        break
    h += constant
    f -= constant
    if the_maze[e][f][g][h] == wall:
        the_maze[e][f][g][h] = down
        the_maze[e][f + 1][g][h] = up
    else:
        break
    constant += 1


print_maze(the_maze, length, width, depth, space)  # prints the maze to begin the fun!
