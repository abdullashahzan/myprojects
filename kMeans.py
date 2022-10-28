import random

# This is the maze
maz= """
DDDDDDD
D0A000D
D0D0D0D
D00DB0D
DDDDDDD
"""

dcnpl = []
stepstaken = 0
finished = False

# This is the process for computer to read the maze
maze = []
count = 0
lmaz = maz.strip().split()
for i in lmaz:
    nmaz = " ".join(i).split()
    maze.insert(count, nmaz)
    count += 1

for j in maze:
    print(j)

def getpos():
    rw, cl = 0, 0
    row = 0
    for j in maze:
        col = 0
        for k in j:
            if k == "A":
                rw, cl = row, col
                break
            else:
                col += 1
        row += 1
    return rw, cl

def look():
    row, col = getpos()
    left, right, up, down = maze[row][col - 1], maze[row][col + 1], maze[row - 1][col], maze[row + 1][col]
    return up, down, left, right

def way():
    global finished
    opt, way, lst = look(), 1, []
    if "B" in opt:
        finished = True
        stop()
    else:
        for i in opt:
            if i != "D" and i != "-":
                lst.append(way)
                way += 1
            else:
                way += 1
    return lst

def move(direction):
    global stepstaken
    row, col = getpos()
    direction = direction[0]
    if direction == 3:
        maze[row][col - 1] = "A"
    elif direction == 4:
        maze[row][col + 1] = "A"
    elif direction == 1:
        maze[row - 1][col] = "A"
    elif direction == 2:
        maze[row + 1][col] = "A"
    maze[row][col] = "-"
    stepstaken += 1
    man()
    return

def dcnp():
    crow, ccol = getpos()
    maze[crow][ccol] = "X"
    orow, ocol = dcnpl[-1][-1][0], dcnpl[-1][-1][1]
    maze[orow][ocol] = "A"
    dcnpl.pop(-1)
    man()
    return

def man():
    global stuck
    opt = way()
    if finished == False:
        if len(opt) > 1:
            choice = random.choices(opt)
            row, col = getpos()
            dcnpl.append([opt, choice, [row, col]])
            move(choice)
        elif len(opt) == 0:
            dcnp()
        else:
            move(opt)
    return

def stop():
    print("\n")
    for i in maze:
        print(i)
    print(f"steps taken: {stepstaken}")
    return

man()






