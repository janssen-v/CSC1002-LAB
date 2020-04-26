## The Snake Game
import turtle as disp
from random import randrange

## WORLD CONFIGURATION
# Window
disp.title('Snake by Vincentius Janssen')  # Initial title screen
disp.setup(520, 520)                       # Made bigger than playable area because in some devices
disp.tracer(0)                             # the window will obscure part of the game area, occasionally.

# Screen
width  = 500
height = 500
bgColor = 'white'
disp.screensize(width, height, bgColor)    # Playable Game Area
blockDist = 20                             # Distance between each block

# Border
border = disp.Turtle()                     # Not part of STATIC ENTITY because
border.ht()                                # border considered as world object
border.pu()
border.speed(0)

# Draw Border
border.setposition(250, 250)
border.pd()
for side in range(4):
    border.right(90)
    border.forward(500)

# REUSABLE FUNCTIONS
def getRoundPos(unit, xy):                 # Defined a function to get rounded position, because there was one time
    unitPosX = int(round(unit.xcor(),2))   # during testing that a float was off by a very small amount that caused    
    unitPosY = int(round(unit.ycor(),2))   # a mismatch in the game checks, causing boundary clipping. By defining
    if xy == 'x':                          # this as a function, the rounding can be implemented more readably.
        return unitPosX
    elif xy == 'y':
        return unitPosY
    elif xy == 'xy':
        return (unitPosX, unitPosY)

## TURTLE ATTRIBUTES
# Title Screen (Turtle)
title = disp.Turtle()
title.pu()
title.ht()
title.color('black')

# Snake (Turtle)
snake = disp.Turtle()
snake.pu()
snake.ht()
snake.speed(0) # Draw speed
snake.shape('square')

# Monster (Turtle)
monster = disp.Turtle()
monster.pu()
monster.ht()
monster.speed(0)
monster.color('purple')
monster.shape('square')

# Food (Turtle)
nFood = disp.Turtle()
nFood.pu()
nFood.ht()
nFood.speed(0)             # It looks better when speed is 10, maybe next time

## GLOBAL OBJECT ATTRIBUTES
# Snake (Object)
snakePaused = False        # Flag for snake state. (Pause = True, Move = False)
outOfBound = False         # Flag for boundary. (Inside = False, Outside = True)
snakeRefSpd = 250          # Refresh Speed of Snake (move speed)
snakeLen = 6
snakeTailCount = 0
snakeHeadPos = getRoundPos(snake, 'xy')
snakeTailPos = []          # list of all current positions of snake tail, used for collision detection
snakeTailExt = False       # Flag for snake tail extension (Fully extended = True)
# Monster (Object)
monTailHit = 0             # Times that monster collides with snake tail

# Food (Object)
nFoodPos = []              # List of all food positions

# Game (Status)
gameOver = False
timeElapsed = 0            # Total in-game time

## ENTITY MOTION LOGIC
# Directional Headings
up = 90    
down = 270
left = 180
right = 0

def turnUp(obj=snake):              # Initially the turn function was going to be used for both snake and monster
    if obj.heading() != down:       # but it was unreliable, so it is only used for the snake now, left it with
        obj.setheading(up)          # obj instead of changing it to snake to keep it modular for future changes.

def turnDown(obj=snake):
    if obj.heading() != up:
        obj.setheading(down)

def turnLeft(obj=snake):
    if obj.heading() != right:
        obj.setheading(left)

def turnRight(obj=snake):
    if obj.heading() != left:
        obj.setheading(right)

def attemptMove():
    global outOfBound
    curX = getRoundPos(snake, 'x')
    curY = getRoundPos(snake, 'y')
    boundary = range(-250,251,1)

    if snake.heading() == up:
        nextY = curY + blockDist  # Used this instead of snake.forward because more reliable, it was often confused because position was returned in floats
        if nextY in boundary:     # although since then position is returned rounded with getRoundPos, this movement method is kept for redundancy to ensure
            outOfBound = False        # that the game will function reliably under all conditions.
            snake.sety(nextY)
        else:
            outOfBound = True

    if snake.heading() == down:
        nextY = curY - blockDist
        if nextY in boundary:
            snake.sety(nextY)
        else:
            outOfBound = True

    if snake.heading() == left:
        nextX = curX - blockDist
        if nextX in boundary:
            outOfBound = False
            snake.setx(nextX)
        else:
            outOfBound = True

    if snake.heading() == right:
        nextX = curX + blockDist
        if nextX in boundary:
            outOfBound = False
            snake.setx(nextX)
        else:
            outOfBound = True

# Snake Pause
def pause():                        # Toggle Snake Pause Flag
    global snakePaused
    if snakePaused != False:
        snakePaused = False
    else:
        snakePaused = True

# GAME CHECKS
def colCheck(pos, hazard):          # The hazard is a tuple of coordinates inside a list in the first and second index
    for i in range(len(hazard)):
        register = hazard[i]
        x = int(register[0])
        y = int(register[1])
        if (x,y) == pos:            # or (x-1,y) == pos or (x+1,y) == pos or (x-1,y-1) == pos or (x-1,y+1) == pos or (x+1,y+1) == pos or (x+1,y-1) == pos or (x,y-1) == pos or (x,y+1) == pos: -> DEPRECATED since no longer using obj.forward
            return (hazard[i], i)   # If none is returned there is no collision, otherwise the coordinates are returned, i is returned for indexing the tuple in the list

def statusCheck():                  # checks victory condition and updates topbar status
    global timeElapsed
    global gameOver
    global snakeTailExt
    timeElapsed += (snakeRefSpd/1000)
    if gameOver or (len(nFoodPos) == 0 and snakeTailExt == True): 
        gameOver = True
        title.setpos(0,0)
        if len(nFoodPos) == 0:
            title.color('green')
            title.write("WINNER !!!"\
                , False, align='center', font=('arial', 25, 'bold'))
        else:
            title.color('red')
            title.write("GAME OVER !!!"\
                , False, align='center', font=('arial', 25, 'bold'))
    else:
        disp.title(('Snake | Contacted: ' + str(monTailHit) + ' , Time Elapsed: ' + str(round(timeElapsed,1)) + 's'))

## CREATE STATIC ENTITY
def spawnTitleScr():
    title.setpos(-220, 190)
    title.write("Welcome to Vincent's version of Snake ...."\
        , False, align='left', font=('arial', 12, 'bold'))
    title.setpos(-220,160)
    title.write("You are going to use the 4 arrow keys to move the snake"\
        , False, align='left', font=('arial', 12, 'bold'))
    title.setpos(-220,140)
    title.write("around the screen, trying to consume all the food items"\
        , False, align='left', font=('arial', 12, 'bold'))
    title.setpos(-220,120)
    title.write("before the monster catches you ...."\
        , False, align='left', font=('arial', 12, 'bold'))
    title.setpos(-220,90)
    title.write("Click anywhere on the screen to start the game, have fun !!"\
        , False, align='left', font=('arial', 12, 'bold'))

def spawnSnake():                   # Not neccessary, but added to make things consistent
    stSnakeH()
    snake.st()

def spawnMonster():
    monster.st()
    while True:
        posX = int(randrange(-12,12,1)*blockDist)
        posY = int(randrange(-12,4,1)*blockDist) # Max spawn in Y dimension is 4, so it doesn't cover the title
        dX = abs(posX - 0)
        dY = abs(posY - 0)
        if dX >= 8*blockDist and dY >= 8*blockDist:
            break
    monster.goto(posX, posY)

def spawnFood():
    for i in range(9):
        posX = int(randrange(-12,12,1)*blockDist)
        posY = int(randrange(-12,12,1)*blockDist)
        nFood.shape('square')
        nFood.color('red')
        nFood.goto(posX, posY)
        stampId = nFood.stamp()
        nFoodPos.append([posX, posY, i+1, stampId]) # The stamp is placed last so that collision detector can be used with different lists
        nFood.color('white')
        nFood.goto(posX, posY-10) # Centers the number printed on the stamp
        nFood.write(i+1, True, align="center", font=("Arial", 12, "bold"))

## ENTITY FUNCTIONS
# Snake (Entity Functions)
def stSnakeH():                    # Used to switch between head and tail stamps
    snake.color('black', 'yellow')
def stSnakeT():
    snake.color('yellow', 'black')

def drawTail():
    global snakeLen
    global snakeTailCount
    global snakeTailPos
    global snakeHeadPos # Because the head needs to start at someplace, since tailpos requires it in line 149
    global snakeRefSpd
    global snakeTailExt
    if not outOfBound:
            snakeTailPos.append(snakeHeadPos) #Append (prev)snake head pos as snaketail pos
            snakeHeadPos = (getRoundPos(snake, 'x'), getRoundPos(snake, 'y')) #Get current position and mark as (new) snake head pos
            collisionHazard = colCheck(snakeHeadPos, nFoodPos)
            
            if collisionHazard != None: # If there is collision
                snakeLen += collisionHazard[0][2] # Add length to snake
                nFood.clearstamp(collisionHazard[0][3])
                del nFoodPos[collisionHazard[1]]  # Deletes food from the list

            stSnakeT() # Switch to draw snake tail
            snake.stamp()
            stSnakeH() # Switch to draw snake head

            if snakeTailCount == snakeLen:
                snakeTailExt = True
                snakeRefSpd = 250
                snake.clearstamps(1)
                del snakeTailPos[0]
            else:
                snakeTailExt = False
                snakeRefSpd = 400 # Snake is slowed when tail not fully extended
                snakeTailCount += 1

## DYNAMIC ENTITY REFRESH
# Snake (Refresh)
def refSnake():
    global snakeRefSpd
    if not snakePaused and gameOver == False: # Checks if paused or if game is over
        attemptMove()
        drawTail()  # draw snake tail
    disp.update()   # design specification asked for manual display update
    statusCheck()
    disp.ontimer(refSnake, snakeRefSpd)

# Monster (Refresh)
def refMon():
    global gameOver
    global monTailHit
    monRefSpd = randrange(250, 500, 50) # Generate random refresh speed (Have tested, it is possible to win with this setting)
    dX = getRoundPos(monster, 'x') - getRoundPos(snake, 'x')
    dY = getRoundPos(monster, 'y') - getRoundPos(snake, 'y')

    if abs(dX) >= abs(dY) and gameOver == False: # if dX > dY, move X, otherwise move Y
        x = getRoundPos(monster, 'x')
        if dX > 0: # if monster is to right of snake, move left, otherwise move right
            monster.setx(x - blockDist)
        elif dX < 0:
            monster.setx(x + blockDist)

    elif abs(dY) >= abs(dX) and gameOver == False:
        y = getRoundPos(monster, 'y')
        if dY > 0: # if monster is above snake, move down, otherwise move up
            monster.sety(y - blockDist)
        elif dY < 0:
            monster.sety(y + blockDist)

    if colCheck(getRoundPos(monster, 'xy'), snakeTailPos) != None: # if there is collision
        monTailHit += 1
    if colCheck(getRoundPos(monster, 'xy'), [getRoundPos(snake, 'xy')]) != None: # if there is collision
        gameOver = True
    disp.update() # design specification asked for manual display update
    disp.ontimer(refMon, monRefSpd)

## EVENT TRIGGERS
# Movement Keybinds
disp.listen()
disp.onkey(turnUp, 'Up')
disp.onkey(turnDown, 'Down')
disp.onkey(turnLeft, 'Left')
disp.onkey(turnRight, 'Right')
disp.onkey(pause, 'space')

# Start Game (On Click)
def clickStart(a, b):
    title.clear()
    disp.onscreenclick(None)
    spawnFood()
    refSnake()
    refMon()

if __name__ == "__main__":
    spawnTitleScr()
    spawnSnake()
    spawnMonster()
    disp.update()
    disp.onscreenclick(clickStart)
    disp.mainloop()
