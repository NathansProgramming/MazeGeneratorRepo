import random


# this text controls what the file name is. Default is 'MazeTrial3D.txt'
file = 'MazeTrial3D.txt'

# this text controls what you see. Default is 'C', '#', 'U', 'D'.
cell = 'C'
wall = '#'
up = 'U'
down = 'D'

# these control how big your maze is. Change them to what you want.
# 4x4x1 is the smallest you can go with it.
length = 10
width = 10
depth = 10


# 3d maze coordinate logic works rather similarly to 2d maze coordinate logic, except with the added z.
# due to depth being added, the new coordinate system is (z, y, x) and depth starts at the top and goes to the bottom.
def make_3d_maze(ln, wd, dp):
    """Creates maze by making a triple nested list with all the characters being walls."""
    maze = []  # the list that will hold the maze.
    for z in range(0, dp):  # keep making boards of lines for how much the depth is.
        board = []  # a board stores a series of lines.
        for y in range(0, wd):  # keep making lines of characters for how much width there is.
            line = []  # a line stores characters.
            for x in range(0, ln):
                line.append(wall)  # appends a wall to the list
            board.append(line)  # appends the list to the board once all of the walls have been appended.
        maze.append(board)  # appends the board to the maze once all of the lines have been appended.
    return maze  # once finished, return the maze.


def print_maze(maze, ln, wd, dp):
    with open(file, 'a') as draw:
        draw.write("\n")
        """Prints the maze with colors (or not) in an organized and easy to read way."""
        for z in range(0, dp):  # for as many boards as there are in the maze
            for y in range(0, wd):  # for as many lines as there are in the board
                for x in range(0, ln):  # for as many characters as there are in the line
                    if maze[z][y][x] == cell:  # if the character is a cell, make it a cell.
                        draw.write(cell + " ")
                    elif maze[z][y][x] == wall:  # if the character is a wall, make it a wall.
                        draw.write(wall + " ")
                    elif maze[z][y][x] == up:  # if the character is an up, make it an up.
                        draw.write(up + " ")
                    else:  # if the character is a down or an invalid character is shown, make it a down.
                        draw.write(down + " ")
                draw.write("\n")
            draw.write("\n")


the_maze = make_3d_maze(length, width, depth)  # create the maze based on the length, width and depth specified.
# I'm sorry if it hurts you that all the following code below is not in a def function. I made it to be simple.

starting_z = random.randint(0, depth-1)  # makes a random z-coordinate
starting_y = random.randint(0, width-1)  # makes a random y-coordinate
starting_x = random.randint(0, length-1)  # makes a random x-coordinate

# here, we make sure that the starting coordinate cell isn't going to clip into a wall.
# if you're wondering why it's -2 on some of them instead of just -1, it's just to be safe on the bug side.
# honestly, the -2's could be removed. Could be a potential test just to see how it functions.
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
# depth doesn't need this check because unlike the last two, it does not require specific positioning.

# make the random start position in the maze a cell.
the_maze[starting_z][starting_y][starting_x] = cell

# add in the walls that are around the beginning cell to begin the fun.
walls = [[starting_z, starting_y - 1, starting_x], [starting_z, starting_y, starting_x - 1],
         [starting_z, starting_y, starting_x + 1], [starting_z, starting_y + 1, starting_x],
         [starting_z - 1, starting_y, starting_x], [starting_z + 1, starting_y, starting_z]]

while len(walls) > 0:  # while there are still walls in the walls list. Yes, it does have to be len(walls).
    rando_choice = random.randint(0, len(walls) - 1)  # gets a random index to choose from
    random_wall = walls[rando_choice]  # uses that random index to get a random wall from the walls list.
    if random_wall[0] < 0 or random_wall[0] > depth - 1:  # if the wall is out of bounds, remove and start again.
        del walls[rando_choice]
        continue
    if random_wall[1] < 1 or random_wall[1] > width - 2:
        del walls[rando_choice]
        continue
    if random_wall[2] < 1 or random_wall[2] > length - 2:
        del walls[rando_choice]
        continue
    if the_maze[random_wall[0]][random_wall[1]][random_wall[2]] != wall:  # if the "wall" isn't a wall, remove.
        del walls[rando_choice]
        continue

    # keeps track of how many cells are nearby the wall. In dimensions of 3 and higher, it has to be ONLY 1.
    # if the cell count is 1, that wall turns into a cell or other equivalent. If lower or higher, forget and remove.
    cell_count = 0
    if random_wall[0] - 1 < 0:  # if the random wall's neighbor is out of bounds, don't check if it's a cell.
        cell_count = cell_count  # random code to do something other than nothing or something bad
    elif the_maze[random_wall[0] - 1][random_wall[1]][random_wall[2]] != wall:  # if the neighbor isn't a wall, increment cell count.
        cell_count += 1

    if random_wall[0] + 1 > depth - 1:
        cell_count = cell_count
    elif the_maze[random_wall[0] + 1][random_wall[1]][random_wall[2]] != wall:
        cell_count += 1

    if random_wall[1] - 1 < 0:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1] - 1][random_wall[2]] != wall:
        cell_count += 1

    if random_wall[1] + 1 > width - 1:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1] + 1][random_wall[2]] != wall:
        cell_count += 1

    if random_wall[2] - 1 < 0:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1]][random_wall[2] - 1] != wall:
        cell_count += 1

    if random_wall[2] + 1 > length - 1:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1]][random_wall[2] + 1] != wall:
        cell_count += 1

    if cell_count == 1:  # if the wall passed the skill check, determine where the one cell it came from was at.
        while True:  # this loop is used primarily to catch bugs, but is also just a nice safety net in general.
            if random_wall[0] - 1 < 0:
                cell_count = cell_count
                # note that "is a cell" down below really means "isn't a wall"
            elif the_maze[random_wall[0] - 1][random_wall[1]][random_wall[2]] != wall:  # if the block above is a cell,
                the_maze[random_wall[0] - 1][random_wall[1]][random_wall[2]] = down  # make it a down
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]] = up  # make the current block an up.
                break

            if random_wall[0] + 1 > depth - 1:
                cell_count = cell_count
            elif the_maze[random_wall[0] + 1][random_wall[1]][random_wall[2]] != wall:  # if the block below is a cell,
                the_maze[random_wall[0] + 1][random_wall[1]][random_wall[2]] = up  # make it an up
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]] = down  # make the current block a down.
                break

            if random_wall[1] - 1 < 0:
                cell_count = cell_count
            elif the_maze[random_wall[0]][random_wall[1] - 1][random_wall[2]] != wall:  # if the block north is a cell,
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]] = cell  # make the current block a cell.
                break

            if random_wall[1] + 1 > width - 1:
                cell_count = cell_count
            elif the_maze[random_wall[0]][random_wall[1] + 1][random_wall[2]] != wall:  # if the block south is a cell,
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]] = cell  # make the current block a cell.
                break

            if random_wall[2] - 1 < 0:
                cell_count = cell_count
            elif the_maze[random_wall[0]][random_wall[1]][random_wall[2] - 1] != wall:  # if the block west is a cell,
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]] = cell  # make the current block a cell.
                break

            if random_wall[2] + 1 > length - 1:
                cell_count = cell_count
            elif the_maze[random_wall[0]][random_wall[1]][random_wall[2] + 1] != wall:  # if the block east is a cell,
                the_maze[random_wall[0]][random_wall[1]][random_wall[2]] = cell  # make the current block a cell.
                break

        # attempt to add all neighboring walls, including ones above and below the cell.
        try:
            walls.append([random_wall[0] - 1, random_wall[1], random_wall[2]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0] + 1, random_wall[1], random_wall[2]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1] - 1, random_wall[2]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1] + 1, random_wall[2]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1], random_wall[2] - 1])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1], random_wall[2] + 1])
        except IndexError:
            pass

        del walls[rando_choice]  # once done with adding neighboring walls, delete itself in the walls list
    else:  # if the wall had 2 or more cells nearby, delete itself in the walls list and go back to the start
        del walls[rando_choice]

# don't change any of these values. they function on their own.
# these values make sure that an entrance and an exit to the maze are made.
# explanation for how this works can be found in the 2d maze generator. This is similar, but goes in two directions.
a = 0
b = 1
c = 1
the_maze[a][b - 1][c] = cell
constant = 1
while True:
    if constant == 1:
        if the_maze[a][b][c] == wall:
            the_maze[a][b][c] = cell
        else:
            break
    c += constant
    if the_maze[a][b][c] == wall:
        the_maze[a][b][c] = cell
    else:
        break
    c -= constant
    b += constant
    if the_maze[a][b][c] == wall:
        the_maze[a][b][c] = cell
    else:
        break
    b -= constant
    constant += 1

d = depth - 1
e = width - 2
f = length - 2
the_maze[d][e + 1][f] = cell
constant = 1
while True:
    if constant == 1:
        if the_maze[d][e][f] == wall:
            the_maze[d][e][f] = cell
        else:
            break
    e -= constant
    if the_maze[d][e][f] == wall:
        the_maze[d][e][f] = cell
    else:
        break
    e += constant
    f -= constant
    if the_maze[d][e][f] == wall:
        the_maze[d][e][f] = cell
    else:
        break
    f += constant
    constant += 1

print_maze(the_maze, length, width, depth)  # prints the maze to begin the fun!
