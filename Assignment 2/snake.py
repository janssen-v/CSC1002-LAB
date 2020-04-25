## The Snake Game
import turtle as disp
from random import randrange

## Setup Configuration
# Window Resolution
disp.setup(540, 540)

# Game Area Size
pixelSpace = 20 # Distance between each block
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

## In-game Unit Attributes
# Snake Unit (Player)
snake = disp.Turtle()
snake.shape('square')
snake.pu()
snake.speed(0)
snakeLen = 6
snakeMotion = 1 # 1 if moving, 0 if paused
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

## Movement Functions
# Directional Heading
def moveUp(obj=snake):
    if obj.heading() != 270:
        obj.setheading(90) 
def moveDown(obj=snake):
    if obj.heading() != 90:
        obj.setheading(270)
def moveLeft(obj=snake):
    if obj.heading() != 0:
        obj.setheading(180)
def moveRight(obj=snake):
    if obj.heading() != 180:
        obj.setheading(0)

# Forward Movement
def moveSnake():
    snake.forward(pixelSpace)
def moveMonster():
    monster.forward(pixelSpace)
def pause():
    global snakeMotion
    if snakeMotion != 0:
        snakeMotion = 0
    else:
        snakeMotion = 1

# Collision Detector
def collisionCheck(pos, hazard):
    for i in range(len(hazard)):
        register = hazard[i]
        x = int(register[0])
        y = int(register[1])
        print(x,y)
        if (x,y) == pos or (x-1,y) == pos or (x+1,y) == pos or (x-1,y-1) == pos or (x-1,y+1) == pos or (x+1,y+1) == pos or (x+1,y-1) == pos or (x,y-1) == pos or (x,y+1) == pos:
            return (hazard[i], i) # If none is returned, there is no collision, otherwise the coordinates are returned, i is returned to make it easier to delete the tuple in the list

## In-game Item Generators
# Food Object
foodPos = []
nFood = disp.Turtle()
for i in range(9):
    nFood.pu()
    nFood.ht()
    nFood.speed(10)
    posX = int(randrange(-12,12,1)*pixelSpace)
    posY = int(randrange(-12,12,1)*pixelSpace)
    nFood.shape('square')
    nFood.color('red')
    nFood.goto(posX, posY)
    stampId = nFood.stamp()
    foodPos.append([posX, posY, i+1, stampId]) # The stamp is placed last so that collision detector can be used with different lists
    nFood.color('white')
    nFood.goto(posX, posY-10) # Centers the number printed on the stamp
    nFood.write(i+1, True, align="center", font=("Arial", 12, "bold"))

# Movement Keybinds
disp.listen()
disp.onkey(moveUp, 'Up')
disp.onkey(moveDown, 'Down')
disp.onkey(moveLeft, 'Left')
disp.onkey(moveRight, 'Right')
disp.onkey(pause, 'space')

# Snake Entity
def updateSnake():
    global tailStamp
    global snakeLen
    global snakeHeadPos
    global snakeTailPos
    global snakeRefSpd
    if snakeMotion == 1:
        moveSnake()
        snakeTailPos.append(snakeHeadPos) #Append (prev)snake head pos as snaketail pos
        snakeHeadPosX = int(snake.pos()[0]) #Get current position and mark as (new) snake head pos
        snakeHeadPosY = int(snake.pos()[1]) # Needed to seperate to make the value an integer, because sometimes the float is not exact and causes a mismatch
        snakeHeadPos = (snakeHeadPosX, snakeHeadPosY)
        print (snakeHeadPos)
        collisionHazard = collisionCheck(snakeHeadPos, foodPos)
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
            del snakeTailPos[1:]
        else:
            snakeRefSpd = 500 # Snake is slowed when tail not fully extended
            tailStamp += 1
    disp.ontimer(updateSnake, snakeRefSpd)


if __name__ == "__main__":
    updateSnake()
    disp.mainloop()
