## The Snake Game
import turtle as disp
import random

## Setup Configuration
# Window Resolution
disp.setup(540, 540)

# Game Area Size
pixelSpace = 20 # Distance between each block
disp.screensize(500, 500) # Game Area
border = disp.Turtle()
border.hideturtle()
border.penup()
border.speed(0)
border.setposition(250, 250)
border.pendown()
for side in range(4):
    border.right(90)
    border.forward(500)

## In-game Units
# Snake Unit (Player)
snake = disp.Turtle()
snake.shape('square')
snake.penup()
snake.speed(0)
lenSnake = 6
def snakeHead():
    snake.shape('turtle')
    snake.color('red', 'black')
def snakeTail():
    snake.shape('square')
    snake.color('green', 'black')

# Monster Unit (Enemy)
monster = disp.Turtle()
monster.color('purple')
monster.shape('square')
monster.penup()
monster.speed(0)

# Moveable Objects
gameObj = [snake, monster]

## Movement Functions
# Directional Heading
def moveUp():
    snake.setheading(90)
def moveDown():
    snake.setheading(270)
def moveLeft():
    snake.setheading(180)
def moveRight():
    snake.setheading(0)

# Forward Movement
def moveSnake():
    snake.forward(pixelSpace)
def moveMonster():
    monster.forward(pixelSpace)

## In-game Items
# Food Object
def food():
    for i in range(9):
        nFood = (i+1 for i in range(9))
        nFood = disp.Turtle()
        x = random.randrange(-10,10,1)
        y = random.randrange(-10,10,1)
        nFood.hideturtle()
        nFood.penup()
        nFood.shape("square")
        nFood.color("red")
        nFood.goto(x*pixelSpace,y*pixelSpace)
        nFood.stamp()

# Movement Keybinds
disp.listen()
disp.onkey(moveUp(), 'Up')
disp.onkey(moveDown(), 'Down')
disp.onkey(moveLeft(), 'Left')
disp.onkey(moveRight(), 'Right')

# Snake Refresher
stamp = 0
speed = 250

def updateSnake():
    global stamp
    global speed
    global lenSnake
    correctLength = False
    moveSnake()
    snakeTail() # Snake tail
    snake.stamp()
    snakeHead() # Snake head
    if stamp == lenSnake:
        snake.clearstamps(1)
    else:
        stamp += 1
    disp.ontimer(updateSnake, speed)

# Collision Detector

if __name__ == "__main__":
    food()
    updateSnake()
    disp.mainloop()
