## The Snake Game
import turtle as disp
from random import randrange

## Setup Configuration
# Window Resolution
disp.setup(540, 540)

# Opening Title
title = disp.Turtle()
title.ht()
title.pu()
title.color('black')
title.setpos(0, 150)
title.write("Welcome to Vincent's snake game"\
, False, align='center', font=('arial', 16, 'bold'))

# Game Area Size
blockDist = 20 # Distance between each block
disp.screensize(500, 500) # Game Area
border = disp.Turtle()
border.ht()
border.pu()
border.speed(0)
border.setposition(250, 250)
border.pendown()
for side in range(4):
    border.right(90)
    border.forward(500)

## UNIT ATTRIBUTES

# Snake Unit (Player)
snake = disp.Turtle()
snake.shape('square')
snake.pu()
snake.speed(0)
snakeLen = 6
snakePaused = 0 # 1 if paused, 0 if moving
outOfBound = 0 # 1 if at boundary and moving out of bounds
snakeRefSpd = 250 # Refresh Speed of Snake
def snakeHead():
    snake.color('black', 'yellow')
def snakeTail():
    snake.color('yellow', 'black')
tailStamp = 0
snakeHeadPos = (0,0)
snakeTailPos = []

# Monster Unit (Enemy)
monster = disp.Turtle()
monster.color('purple')
monster.shape('square')
monster.pu()
monster.speed(0)
posX = int(randrange(-12,12,1)*blockDist)
posY = int(randrange(-12,12,1)*blockDist)
monster.goto(posX, posY)
monTailCol = 0 # Times that monster collides with snake tail
monRefSpd = randrange(400, 500, 50)

## MOVE FUNCTIONS

# Get Current Position (with rounding, because sometimes there is a really small error that will mess up functions)
def getPosition(unit, xy):
    unitPosX = int(round(unit.xcor(),2))
    unitPosY = int(round(unit.ycor(),2))
    if xy == 'x':
        return unitPosX
    elif xy == 'y':
        return unitPosY

# Directional Heading
up = 90
down = 270
left = 180
right = 0

def turnUp(obj=snake):          # Initially the turn function was going to be used for both snake and monster
    if obj.heading() != down:   # but it was unreliable, so it is only used for the snake now
        obj.setheading(up) 
def turnDown(obj=snake):
    if obj.heading() != up:
        obj.setheading(down)
def turnLeft(obj=snake):
    if obj.heading() != right:
        obj.setheading(left)
def turnRight(obj=snake):
    if obj.heading() != left:
        obj.setheading(right)

def pause(): # Toggle Snake Pause Flag
    global snakePaused
    if snakePaused != 0:
        snakePaused = 0
    else:
        snakePaused = 1

# GAME CHECKS
def colCheck(pos, hazard): # The hazard is a tuple of coordinates inside a list in the first and second index
    for i in range(len(hazard)):
        register = hazard[i]
        x = int(register[0])
        y = int(register[1])
        if (x,y) == pos: # or (x-1,y) == pos or (x+1,y) == pos or (x-1,y-1) == pos or (x-1,y+1) == pos or (x+1,y+1) == pos or (x+1,y-1) == pos or (x,y-1) == pos or (x,y+1) == pos:
            return (hazard[i], i) # If none is returned, there is no collision, otherwise the coordinates are returned, i is returned to make it easier to delete the tuple in the list


def attemptMove(): # Move to production
    global outOfBound
    curX = snake.xcor()
    curY = snake.ycor()
    boundary = range(-250,251,1)

    if snake.heading() == up: # Used this instead of snake.forward because more reliable
        nextY = curY + blockDist
        if nextY in boundary:
            outOfBound = 0
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


def statusCheck(): #checks victory condition and updates topbar status
    pass

## CREATE ENTITY
# Food Object
foodPos = []
nFood = disp.Turtle()
for i in range(9):
    nFood.pu()
    nFood.ht()
    nFood.speed(10)
    posX = int(randrange(-12,12,1)*blockDist)
    posY = int(randrange(-12,12,1)*blockDist)
    nFood.shape('square')
    nFood.color('red')
    nFood.goto(posX, posY)
    stampId = nFood.stamp()
    foodPos.append([posX, posY, i+1, stampId]) # The stamp is placed last so that collision detector can be used with different lists
    nFood.color('white')
    nFood.goto(posX, posY-10) # Centers the number printed on the stamp
    nFood.write(i+1, True, align="center", font=("Arial", 12, "bold"))

## DYNAMIC ENTITIES
# Snake Entity
def updateSnake():
    global tailStamp
    global snakeLen
    global snakeHeadPos # Because the head needs to start at someplace, since tailpos requires it in line 149
    global snakeTailPos
    global snakeRefSpd
    

    if snakePaused == 0:
        attemptMove()
        if outOfBound == 0:
            snakeTailPos.append(snakeHeadPos) #Append (prev)snake head pos as snaketail pos
            snakeHeadPos = (getPosition(snake, 'x'), getPosition(snake, 'y')) #Get current position and mark as (new) snake head pos
            print (snakeHeadPos) # DEBUG #1
            collisionHazard = colCheck(snakeHeadPos, foodPos)
            if collisionHazard != None: # If there is collision
                snakeLen += collisionHazard[0][2] # Add length to snake
                nFood.clearstamp(collisionHazard[0][3])
                del foodPos[collisionHazard[1]]  # Deletes food from the list
            snakeTail() # Switch to draw snake tail
            snake.stamp()
            snakeHead() # Switch to draw snake head
            if tailStamp == snakeLen:
                snakeRefSpd = 250
                snake.clearstamps(1)
                del snakeTailPos[1]
                # Insert Win Condition Check Here
            else:
                snakeRefSpd = 500 # Snake is slowed when tail not fully extended
                tailStamp += 1
    disp.ontimer(updateSnake, snakeRefSpd)

# Monster Entity
def updateMonster():
    global monRefSpd
    global monTailCol
    # Measure future distance to snake with math in all four axes, go to place closest to snake
    dX = monster.xcor() - snake.xcor()
    dY = monster.ycor() - snake.ycor()
    if abs(dX) >= abs(dY): # if dX > dY, move X, otherwise move Y
        x = monster.xcor()
        if dX > 0: # if monster is to right of snake, move left, otherwise move right
            monster.setx(x - blockDist)
        elif dX < 0:
            monster.setx(x + blockDist)
    elif abs(dY) >= abs(dX):
        y = monster.ycor()
        if dY > 0: # if monster is above snake, move down, otherwise move up
            monster.sety(y - blockDist)
        elif dY < 0:
            monster.sety(y + blockDist)

    monsterPos = (getPosition(monster, 'x'), getPosition(snake, 'x'))
    if colCheck(monsterPos, snakeTailPos) != None: # if there is collision
        monTailCol += 1
    if colCheck(monsterPos, [snakeHeadPos]) != None: # if there is collision
        gameOver = True
    disp.ontimer(updateMonster, monRefSpd)

## LISTEN FOR EVENTS
# Movement Keybinds
disp.listen()
disp.onkey(turnUp, 'Up')
disp.onkey(turnDown, 'Down')
disp.onkey(turnLeft, 'Left')
disp.onkey(turnRight, 'Right')
disp.onkey(pause, 'space')

# Click Binds
def clickStart():
    pass

if __name__ == "__main__":
    disp.update()
    updateSnake()
    updateMonster()
    disp.mainloop()
