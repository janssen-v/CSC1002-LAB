# The Snake Game
import turtle as disp

# Initial Configurations
width = 500
height = 500
bgcolor = 'white'
disp.screensize(width, height, bgcolor)

# Game Characters
# Snake unit
snake = disp.Turtle()
snake.color('black')
snake.shape('square')
snake.penup()
snake.speed(0)
lenSnake = 5

# Monster Unit
monster = disp.Turtle()
monster.color('purple')
monster.shape('square')
monster.penup()
monster.speed(0)

# Food Object
food = disp.Turtle()

gameChars = [snake, monster]

# Refresh Tick

def update():
    snake.forward(1)
    disp.ontimer(update, 1)

# Snake turns

def moveUp():
    for unit in gameChars:
        unit.setheading(90)

def moveDown():
    for unit in gameChars:
        unit.setheading(270)

def moveLeft():
    for unit in gameChars:
        unit.setheading(180)

def moveRight():
    for unit in gameChars:
        unit.setheading(0)
    
# Keybinds
disp.listen()
disp.onkey(moveUp, 'Up')
disp.onkey(moveDown, 'Down')
disp.onkey(moveLeft, 'Left')
disp.onkey(moveRight, 'Right')

# Collision Detector


def moveSnake():
    snake.forward(15)
    
stamp = 0
def update():
    global stamp
    lenSnake = 5
    correctLength = False
    snake.stamp()
    moveSnake()
    if stamp == lenSnake:
        snake.clearstamps(1)
    else:
        stamp += 1
    disp.ontimer(update, 200)
    

if __name__ == "__main__":
    update()
    disp.mainloop()
