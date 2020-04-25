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
    obj.setheading(90) 
def moveDown(obj=snake):
    obj.setheading(270)
def moveLeft(obj=snake):
    obj.setheading(180)
def moveRight(obj=snake):
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
    posX = pos[0]
    posY = pos[1]
    for i in range(len(hazard)):
        register = hazard[i]
        if posX == register[0] and posY == register[1]:
            return (hazard[i]) # If none is returned, there is no collision, otherwise the coordinates are returned

## In-game Item Generators
# Food Object
foodPos = []
nFood = disp.Turtle()
for i in range(9):
    nFood.pu()
    nFood.ht()
    nFood.speed(10)
    posX = randrange(-12,12,1)*pixelSpace
    posY = randrange(-12,12,1)*pixelSpace
    nFood.shape('square')
    nFood.color('red')
    nFood.goto(posX, posY)
    stampId = nFood.stamp()
    foodPos.append([posX, posY, i+1, stampId]) # Marks the position of the food
                                      # The value is placed last so that collision checker can work with more than just this type of tuple
    nFood.color('white')
    nFood.goto(posX, posY-10)
    nFood.write(i+1, True, align="center", font=("Arial", 12, "bold"))
    print(foodPos)
    #append the xy position to a list and if the snake passes that position
    #commit action

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
    global snakeHeadPos
    global snakeTailPos
    global snakeLen
    if snakeMotion == 1:
        moveSnake()
        snakeTailPos.append(snakeHeadPos) #Append (prev)snake head pos as snaketail pos
        snakeHeadPos = (snake.pos()) #Get current position and mark as (new) snake head pos
        collisionHazard = collisionCheck(snakeHeadPos, foodPos)
        if collisionHazard != None: # If there is a collision
            snakeLen += collisionHazard[2] # Add length
            print (collisionHazard[3])
            nFood.clearstamp(collisionHazard[3])
            nFood.clearstamp(collisionHazard[3])

        snakeTail() # Snake tail
        snake.stamp()
        snakeHead() # Snake head
        if tailStamp == snakeLen:
            snake.clearstamps(1)
            del snakeTailPos[1:]
        else:
            tailStamp += 1
    disp.ontimer(updateSnake, snakeRefSpd)



if __name__ == "__main__":
    updateSnake()
    disp.mainloop()
