import pygame, random

began, found, debug = True, False, False
ids, stepstaken, uid = 100, 0, 9
oldgen = []

class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.rand = random.randint(0, 8)
        return
    def validate_maze(maze):
        global grid
        for i in range(0,60):
            maze[random.randint(0, 7)][random.randint(0, 7)] = 1
        while True:
            row, col = random.randint(0, 7), random.randint(0, 7)
            if maze[row][col] == 1:
                maze[row][col] = 5
                while True:
                    row2, col2 = random.randint(0, 7), random.randint(0, 7)
                    if maze[row2][col2] == 1:
                        maze[row2][col2] = 7
                        break
                break
        grid = maze
        return
    def create_maze():
        maze = []
        row = []
        for i in range(8):
            for j in range(8):
                row.append(0)
            maze.append(row)
            row = []
        Maze.validate_maze(maze)
        return

class alpha:
    def __init__(self):
        return
    def solve():
        global began, oldgen
        if began == True:
            for i in grid:
                for j in i:
                    if j == 7:
                        began = False
                        identity = 7
                        position = alpha.getpos(identity)
                        opt = alpha.option(position)
                        alpha.move(opt)
        elif began == False:
            for k in oldgen:
                oldgen.remove(k)
                for l in grid:
                    for m in l:
                        if m == k:
                            identity = k
                            position = alpha.getpos(identity)
                            opt = alpha.option(position)
                            alpha.move(opt)
        return
    def option(pos):
        global found
        options = []
        row, col = pos[0], pos[1]
        if col != 7:
            if grid[row][col + 1] == 1:
                options.append([row, col + 1])
            elif grid[row][col + 1] == 5:
                found = True
                print("Found!")
        if col != 0:
            if grid[row][col - 1] == 1:
                options.append([row, col - 1])
            elif grid[row][col - 1] == 5:
                found = True
                print("Found!")
        if row != 7:
            if grid[row + 1][col] == 1:
                options.append([row + 1, col])
            elif grid[row + 1][col] == 5:
                found = True
                print("Found!")
        if row != 0:
            if grid[row - 1][col] == 1:
                options.append([row - 1, col])
            elif grid[row - 1][col] == 5:
                found = True
                print("Found!")
        return options
    def getpos(identity):
        row = 0
        for i in grid:
            col = 0
            for j in i:
                if j == identity:
                    return [row, col]
                else:
                    col += 1
            row += 1
    def move(steps):
        global ids, oldgen, stepstaken
        stepstaken += 1
        for i in steps:
            oldgen.append(ids)
            grid[i[0]][i[1]] = ids
            ids += 1
        return

class beta:
    def __init__(self):
        return
    def solve():
        rc = beta.pos()
        opt = beta.option(rc)
        if len(opt) > 1:
            for i in opt:
                beta.move(i)
        elif len(opt) == 1:
            beta.move(opt[0])
        return
    def option(rowcol):
        global found
        options = []
        row, col = rowcol[0], rowcol[1]
        if col != 7:
            if grid[row][col + 1] == 1:
                options.append([row, col + 1])
            elif grid[row][col + 1] == 5:
                found = True
                print("Found!")
        if col != 0:
            if grid[row][col - 1] == 1:
                options.append([row, col - 1])
            elif grid[row][col - 1] == 5:
                found = True
                print("Found!")
        if row != 7:
            if grid[row + 1][col] == 1:
                options.append([row + 1, col])
            elif grid[row + 1][col] == 5:
                found = True
                print("Found!")
        if row != 0:
            if grid[row - 1][col] == 1:
                options.append([row - 1, col])
            elif grid[row - 1][col] == 5:
                found = True
                print("Found!")
        return options
    def pos():
        global began
        if began == True:
            began = False
            row = 0
            for i in grid:
                col = 0
                for j in i:
                    if j == 7:
                        return [row, col]
                    else:
                        col += 1
                row += 1
        elif began == False:
            row = 0
            for i in grid:
                col = 0
                for j in i:
                    if j >= 9 and j <= 99:
                        grid[row][col] = 100
                        return [row, col]
                    else:
                        col +=1
                row += 1
    def move(path):
        global stepstaken, uid
        grid[path[0]][path[1]] = uid
        uid += 1
        stepstaken += 1
    
class gamma:
    def __init__(self):
        return
    def solve():
        global began
        if began == True:
            began = False
            position = gamma.pos(7)
            options = gamma.option(position)
            for i in options:
                gamma.move(i)
        else:
            print("Working...")
        return
    def pos(n):
        row = 0
        for i in grid:
            col = 0
            for j in i:
                if j == n:
                    return [row, col]
                else:
                    col +=1 
            row += 1
    def option(rowcol):
        global found
        options = []
        row, col = rowcol[0], rowcol[1]
        if col != 7:
            if grid[row][col + 1] == 1:
                options.append([row, col + 1])
            elif grid[row][col + 1] == 5:
                found = True
                print("Found!")
        if col != 0:
            if grid[row][col - 1] == 1:
                options.append([row, col - 1])
            elif grid[row][col - 1] == 5:
                found = True
                print("Found!")
        if row != 7:
            if grid[row + 1][col] == 1:
                options.append([row + 1, col])
            elif grid[row + 1][col] == 5:
                found = True
                print("Found!")
        if row != 0:
            if grid[row - 1][col] == 1:
                options.append([row - 1, col])
            elif grid[row - 1][col] == 5:
                found = True
                print("Found!")
        return options
    def move(path):
        grid[path[0]][path[1]] = 100
        return

Maze.create_maze()

windowSize = (419,490)
screen = pygame.display.set_mode(windowSize)
end = False
pygame.init()

WIDTH = 50
HEIGHT = 50
MARGIN = 2
button = pygame.Rect(20, 427, 115, 25)
button2 = pygame.Rect(20,460,115,25)
button3 = pygame.Rect(150, 460, 115, 25) 
button4 = pygame.Rect(280, 460, 115, 25)
button5 = pygame.Rect(150, 427, 115, 25)
button6 = pygame.Rect(280, 427, 115, 25)
smallfont = pygame.font.SysFont('Corbel',15)

def regenerate():
    global began, found, debug
    began, found, debug = True, False, False
    Maze.create_maze()
    return

def dalpha():
    global stepstaken
    if debug == False:
        while found == False:
            alpha.solve()
        print(f"Steps taken: {stepstaken}")
        stepstaken = 0
    else:
        alpha.solve()
    return

def dbeta():
    global stepstaken
    if debug == False:
        while found == False:
            beta.solve()
        print(f"Steps taken: {stepstaken}")
        stepstaken = 0
    else:
        beta.solve()
    return

def dgamma():
    gamma.solve()
    return

def clr():
    global began, found, debug
    began, found, debug = True, False, False
    for i in range(8):
        for j in range(8):
            if grid[i][j] >= 9:
                grid[i][j] = 1
    return

while end != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if button.collidepoint(pos):
                regenerate()
            if button2.collidepoint(pos):
                dalpha()
            if button3.collidepoint(pos):
                dbeta()
            if button4.collidepoint(pos):
                dgamma()
            if button5.collidepoint(pos):
                clr()
            if button6.collidepoint(pos):
                debug = True
                print("Debugging...")
    pygame.draw.rect(screen, [255,0,255], button)
    pygame.draw.rect(screen, [255,255,255], button2)
    pygame.draw.rect(screen, [255,255,255], button3)
    pygame.draw.rect(screen, [255,255,255], button4)
    pygame.draw.rect(screen, [255,255,100], button5)
    pygame.draw.rect(screen, [255,0,255], button6)
    screen.blit(smallfont.render('Re-Generate' , True , (0,0,0)), (40,433))
    screen.blit(smallfont.render('Alpha algorithim' , True , (0,0,0)), (27,465))
    screen.blit(smallfont.render('Beta algorithim' , True , (0,0,0)), (163,465))
    screen.blit(smallfont.render('Gamma algorithim' , True , (0,0,0)), (281,465))
    screen.blit(smallfont.render('Clear' , True , (0,0,0)), (193,433))
    screen.blit(smallfont.render('Debug', True, (0,0,0)), (316,433))
    for row in range(8):
        for column in range(8):
            color = (255,255,255)
            if grid[row][column] == 0:
                color = (0,255,255)
            if grid[row][column] == 7:
                color = (255,0,0)
            if grid[row][column] == 5:
                color = (0,0,255)
            if grid[row][column] >= 9 and grid[row][column] <= 99:
                color = (100,0,100)
            if grid[row][column] >= 100:
                color = (100,100,100)
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
    pygame.display.flip()

pygame.quit()


#Plans : alpha, beta, gamma