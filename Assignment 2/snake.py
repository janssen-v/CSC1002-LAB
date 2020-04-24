# The Snake Game
import turtle as disp
import random

# Initial Configurations
width = 500
height = 500
bgcolor = 'white'
disp.screensize(width, height, bgcolor)

# Game Characters
# Snake Unit
snake = disp.Turtle()
snake.shape('square')
snake.penup()
snake.speed(0)
lenTail = 5
def snakeHead():
    snake
    snake.color('red', 'black')
def snakeTail():
    snake.color('green', 'black')

# Monster Unit
monster = disp.Turtle()
monster.color('purple')
monster.shape('square')
monster.penup()
monster.speed(0)

# Food Object
food = disp.Turtle()
def food(tfood):
    x = random.randrange(-8,8,1)
    y = random.randrange(-8,8,1)
    fcoord[0] = x
    fcoord[1] = y
    tfood.hideturtle()
    tfood.pu()
    tfood.shape("square")
    tfood.color("red")
    tfood.goto(x*20,y*20)
    tfood.stamp()

gameObjs = [snake, monster]

# Refresh Screen
stamp = 0
speed = 200

def updateSnake():
    global stamp
    global speed
    global lenTail
    correctLength = False
    snakeTail() # Snake tail
    snake.stamp()
    snakeHead() # Snake head
    moveSnake()
    if stamp == lenTail:
        snake.clearstamps(1)
    else:
        stamp += 1
    disp.ontimer(updateSnake, speed)

# Unit move
def moveUp():
    for unit in gameObjs:
        unit.setheading(90)
def moveDown():
    for unit in gameObjs:
        unit.setheading(270)
def moveLeft():
    for unit in gameObjs:
        unit.setheading(180)
def moveRight():
    for unit in gameObjs:
        unit.setheading(0)
def moveSnake():
    snake.forward(22)
    
# Keybinds
disp.listen()
disp.onkey(moveUp, 'Up')
disp.onkey(moveDown, 'Down')
disp.onkey(moveLeft, 'Left')
disp.onkey(moveRight, 'Right')

# Collision Detector

if __name__ == "__main__":
    updateSnake()
    disp.mainloop()
