## The Snake Game
import turtle as disp
from random import randrange

## SETUP CONFIG

# Resolution
disp.setup(520, 520) # Made bigger than playable area because in some devices the window will obscure part of the game area

# World
blockDist = 20 # Distance between each block
disp.screensize(500, 500) # Playable Game Area

# Border
border = disp.Turtle()
border.ht()
border.pu()
border.speed(0)

border.setposition(250, 250)
border.pd()
for side in range(4):
    border.right(90)
    border.forward(500)

# Opening Title
title = disp.Turtle()
title.ht()
title.pu()
title.color('black')
title.setpos(0, 150)
title.write("Welcome to Vincent's snake game"\
, False, align='center', font=('arial', 16, 'bold'))


# REUSABLE FUNCTIONS

def getRoundPos(unit, xy):                  # Defined a function to get rounded position, because there was one time
    unitPosX = int(round(unit.xcor(),2))    # during testing that a float was off by a very small amount that caused    
    unitPosY = int(round(unit.ycor(),2))    # a mismatch in the game checks, causing boundary clipping. By defining
    if xy == 'x':                           # this as a function, the rounding can be implemented while being readable.
        return unitPosX
    elif xy == 'y':
        return unitPosY
    elif xy == 'xy':
        return (unitPosX, unitPosY)
        
## OBJECT ATTRIBUTES

# Snake
snake = disp.Turtle()
snake.pu()
snake.speed(0)
snake.shape('square')

snakePaused = 0 # 1 if paused, 0 if moving
outOfBound = 0 # 1 if at boundary and moving out of bounds
snakeRefSpd = 250 # Refresh Speed of Snake

snakeLen = 6
snakeTailCount = 0
snakeHeadPos = getRoundPos(snake, 'xy')
snakeTailPos = []

def snakeHead():
    snake.color('black', 'yellow')
def snakeTail():
    snake.color('yellow', 'black')

# Monster
monster = disp.Turtle()
monster.pu()
monster.speed(0)
monster.color('purple')
monster.shape('square')

while True:
    posX = int(randrange(-12,12,1)*blockDist)
    posY = int(randrange(-12,6,1)*blockDist) # Max spawn in Y dimension is 6, so it doesn't cover the title
    dX = abs(posX - 0)
    dY = abs(posY - 0)
    if dX >= 4*blockDist or dY >= 4*blockDist:
        break

monster.goto(posX, posY)

monTailHit = 0 # Times that monster collides with snake tail
monRefSpd = randrange(400, 500, 50)

# Food
nFood = disp.Turtle()
nFood.pu()
nFood.speed(0) # It looks better when speed is 10, maybe next time
nFood.ht()

nFoodPos = []


## MOVE FUNCTIONS
# Directional Headings
up = 90    
down = 270
left = 180
right = 0

def turnUp(obj=snake):          # Initially the turn function was going to be used for both snake and monster
    if obj.heading() != down:   # but it was unreliable, so it is only used for the snake now, left it with
        obj.setheading(up)      # obj instead of changing it to snake to keep it modular for future changes.

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
            outOfBound = 0        # that the game will function reliably under all conditions.
            snake.sety(nextY)
        else:
            outOfBound = 1

    if snake.heading() == down:
        nextY = curY - blockDist
        if nextY in boundary:
            snake.sety(nextY)
        else:
            outOfBound = 1

    if snake.heading() == left:
        nextX = curX - blockDist
        if nextX in boundary:
            outOfBound = 0
            snake.setx(nextX)
        else:
            outOfBound = 1

    if snake.heading() == right:
        nextX = curX + blockDist
        if nextX in boundary:
            outOfBound = 0
            snake.setx(nextX)
        else:
            outOfBound = 1

# Snake Pause
def pause(): # Toggle Snake Pause Flag
    global snakePaused
    if snakePaused != 0:
        snakePaused = 0
    else:
        snakePaused = 1

# GAME CHECKS
def colCheck(pos, hazard):  # The hazard is a tuple of coordinates inside a list in the first and second index
    for i in range(len(hazard)):
        register = hazard[i]
        x = int(register[0])
        y = int(register[1])
        if (x,y) == pos: # or (x-1,y) == pos or (x+1,y) == pos or (x-1,y-1) == pos or (x-1,y+1) == pos or (x+1,y+1) == pos or (x+1,y-1) == pos or (x,y-1) == pos or (x,y+1) == pos: -> DEPRECATED since no longer using obj.forward
            return (hazard[i], i) # If none is returned there is no collision, otherwise the coordinates are returned, i is returned for indexing the tuple in the list

def statusCheck(): #checks victory condition and updates topbar status
    pass

## CREATE ENTITY
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

## DYNAMIC ENTITIES
# Refresh Snake Entity
def refSnake():
    global snakeTailCount
    global snakeLen
    global snakeHeadPos # Because the head needs to start at someplace, since tailpos requires it in line 149
    global snakeTailPos
    global snakeRefSpd
    
    if snakePaused == 0: # Move these to functions
        attemptMove()

        if outOfBound == 0:
            snakeTailPos.append(snakeHeadPos) #Append (prev)snake head pos as snaketail pos
            snakeHeadPos = (getRoundPos(snake, 'x'), getRoundPos(snake, 'y')) #Get current position and mark as (new) snake head pos
            collisionHazard = colCheck(snakeHeadPos, nFoodPos)
            
            if collisionHazard != None: # If there is collision
                snakeLen += collisionHazard[0][2] # Add length to snake
                nFood.clearstamp(collisionHazard[0][3])
                del nFoodPos[collisionHazard[1]]  # Deletes food from the list

            snakeTail() # Switch to draw snake tail
            snake.stamp()
            snakeHead() # Switch to draw snake head

            if snakeTailCount == snakeLen:
                snakeRefSpd = 250
                snake.clearstamps(1)
                del snakeTailPos[1]
                # Insert Win Condition Check Here
            else:
                snakeRefSpd = 500 # Snake is slowed when tail not fully extended
                snakeTailCount += 1
    disp.ontimer(refSnake, snakeRefSpd)

# Refresh Monster Entity
def refMon():
    global monRefSpd
    global monTailHit
    # Measure future distance to snake with math in all four axes, go to place closest to snake
    dX = getRoundPos(monster, 'x') - getRoundPos(snake, 'x')
    dY = getRoundPos(monster, 'y') - getRoundPos(snake, 'y')

    if abs(dX) >= abs(dY): # if dX > dY, move X, otherwise move Y
        x = getRoundPos(monster, 'x')
        if dX > 0: # if monster is to right of snake, move left, otherwise move right
            monster.setx(x - blockDist)
        elif dX < 0:
            monster.setx(x + blockDist)

    elif abs(dY) >= abs(dX):
        y = getRoundPos(monster, 'y')
        if dY > 0: # if monster is above snake, move down, otherwise move up
            monster.sety(y - blockDist)
        elif dY < 0:
            monster.sety(y + blockDist)

    if colCheck(getRoundPos(monster, 'xy'), snakeTailPos) != None: # if there is collision
        monTailHit += 1
        print('Tail Hit:', monTailHit)
    if colCheck(getRoundPos(monster, 'xy'), [getRoundPos(snake, 'xy')]) != None: # if there is collision
        gameOver = True
        print('Game Over')
    disp.ontimer(refMon, monRefSpd)

## LISTEN FOR EVENTS
# Movement Keybinds
disp.listen()
disp.onkey(turnUp, 'Up')
disp.onkey(turnDown, 'Down')
disp.onkey(turnLeft, 'Left')
disp.onkey(turnRight, 'Right')
disp.onkey(pause, 'space')

# On Click Actions
def clickStart():
    pass

if __name__ == "__main__":
    disp.update()
    spawnFood()
    refSnake()
    refMon()
    disp.mainloop()
