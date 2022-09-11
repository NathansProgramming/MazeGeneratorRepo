import random
# if your computer or device can't run colorama, just delete these two lines and remove "FORE.<color>" in print_maze.
from colorama import init, Fore
init()

# this text controls what you see. Default is 'C', '#'.
cell = 'C'
wall = '#'

# these control how big your maze is. Change them to what you want.
# 3x3 is the smallest you can go with it.
length = 10
width = 10


# a good thing to know is how specifically coordinates work in a double nested list:
# the y coordinate goes first when denoting coordinates, not x. This is because it needs to find what line it's on.
# the coordinate (0,0) is in the top left corner where as the coordinate (width-1, length-1) is in the bottom right.
def make_maze(ln, wd):
    """Creates maze by making a double nested list with all the characters being walls."""
    maze = []  # the list that will be holding the maze
    for y in range(0, wd):  # keep making lines of characters for how much width there is.
        line = []  # lines hold a line of characters.
        for x in range(0, ln):  # keep making characters for how much length there is.
            line.append(wall)  # appends a wall to the list
        maze.append(line)  # appends the list to the maze once all of the walls have been appended.
    return maze  # once finished, return the maze.


def print_maze(maze):
    """Prints the maze with colors (or not) in an organized and easy to read way."""
    for y in range(0, len(maze)):  # for as many lines as there are in the maze
        for x in range(0, len(maze[0])):  # for as many characters as there are in the line
            if maze[y][x] == cell:  # if the character is a cell, make it green.
                print(Fore.GREEN, f'{maze[y][x]}', end="")
            elif maze[y][x] == wall:  # if the character is a wall, make it red.
                print(Fore.RED, f'{maze[y][x]}', end="")
            elif maze[y][x] == 'U':  # foreshadowing for the 3d maze code
                print(Fore.BLUE, f'{maze[y][x]}', end="")
            else:  # if an incorrect or invalid letter is printed, make it yellow.
                print(Fore.YELLOW, f'{maze[y][x]}', end="")
        print('')


the_maze = make_maze(length, width)  # create the maze based on the length and width specified.
# I'm sorry if it hurts you that all the following code below is not in a def function. I just made it to be simple.

starting_y = random.randint(0, width-1)  # makes a random y-coordinate
starting_x = random.randint(0, length-1)  # makes a random x-coordinate

# here, we make sure that the starting coordinate cell isn't going to clip into a wall.
if starting_x == 0:  # if starting_x is on the edge, change the position.
    starting_x += 1
if starting_x == length - 1:  # vice versa.
    starting_x -= 1
if starting_y == 0:  # if the starting_y is on the edge, change the position.
    starting_y += 1
if starting_y == width - 1:  # vice versa.
    starting_y -= 1

# make the random start position in the maze a cell.
the_maze[starting_y][starting_x] = cell

# add in the walls that are around the beginning cell to begin the fun.
walls = [[starting_y - 1, starting_x], [starting_y, starting_x - 1],
         [starting_y, starting_x + 1], [starting_y + 1, starting_x]]

while len(walls) > 0:  # while there are still walls in the walls list. Yes, it does have to be len(walls).
    rando_choice = random.randint(0, len(walls) - 1)  # gets a random index to choose from
    random_wall = walls[rando_choice]  # uses that random index to get a random wall from the walls list.
    if random_wall[0] < 1 or random_wall[0] > width - 2:  # if the wall is out of bounds, remove and start again.
        del walls[rando_choice]
        continue
    if random_wall[1] < 1 or random_wall[1] > length - 2:
        del walls[rando_choice]
        continue
    if the_maze[random_wall[0]][random_wall[1]] == cell:  # if the "wall" is actually a cell, remove and start again.
        del walls[rando_choice]
        continue

    # keeps track of how many cells are nearby the wall. As long as it's less than 2, the wall will become a cell.
    cell_count = 0
    if random_wall[0] - 1 < 0:  # if the random wall's neighbor is out of bounds, don't check if it's a cell.
        cell_count = cell_count  # random code to do something other than nothing or something bad
    elif the_maze[random_wall[0] - 1][random_wall[1]] == cell:  # if the neighbor is a cell, increment cell count.
        cell_count += 1

    if random_wall[0] + 1 > width - 1:
        cell_count = cell_count
    elif the_maze[random_wall[0] + 1][random_wall[1]] == cell:
        cell_count += 1

    if random_wall[1] - 1 < 0:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1] - 1] == cell:
        cell_count += 1

    if random_wall[1] + 1 > length - 1:
        cell_count = cell_count
    elif the_maze[random_wall[0]][random_wall[1] + 1] == cell:
        cell_count += 1

    if cell_count < 2:  # if the wall passed the cell check, make it a cell and try to add the neighboring walls.
        the_maze[random_wall[0]][random_wall[1]] = cell
        try:
            walls.append([random_wall[0] - 1, random_wall[1]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0] + 1, random_wall[1]])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1] - 1])
        except IndexError:
            pass
        try:
            walls.append([random_wall[0], random_wall[1] + 1])
        except IndexError:
            pass
        del walls[rando_choice]  # once done with adding neighboring walls, delete itself in the walls list
    else:  # if the wall had 2 or more cells nearby, delete itself in the walls list and go back to the start
        del walls[rando_choice]


# don't change any of these values. they function on their own.
# these values make sure that an entrance and an exit to the maze are made.
a = 0
b = 1
the_maze[a][b] = cell  # the top second leftmost wall is turned into a cell
while True:
    a += 1
    if the_maze[a][b] == wall:  # if the next cell in front is still a wall, make it a cell.
        the_maze[a][b] = cell
    else:  # stop making cells in front of the entrance when there are no more walls obstructing.
        break

# this part works basically the same above, however makes the exit correct.
c = width - 1
d = length - 2
the_maze[width-1][length-2] = cell
while True:
    c -= 1
    if the_maze[c][d] == wall:
        the_maze[c][d] = cell
    else:
        break

print_maze(the_maze)  # prints the maze to begin the fun!
