# The Snake Game
import turtle as disp

# Initial Configurations
width = 500
height = 500
bgcolor = 'white'
disp.screensize(width, height, bgcolor)

# Objects
objects = ['snake', 'monster']

# Snake unit
snake = disp.Turtle()
snake.color('black')
snake.shape('square')
snake.penup()
snake.speed(0)

# Monster Unit
monster = disp.Turtle()
monster.color('purple')
monster.shape('square')
monster.penup()
monster.speed(0)


# Refresh Tick

def update():
    snake.forward(1)
    disp.ontimer(update, 1)

# Snake turns
def leftTurn():
    snake.left(90)

def rightTurn():
    snake.right(90)

# Keybinds
disp.listen()
disp.onkey(leftTurn, 'Left')
disp.onkey(rightTurn, 'Right')

# Collision Detector

def moveSnake():
    snake.forward(15)

def update():
    moveSnake()
    disp.ontimer(update, 200)

if __name__ == "__main__":
    update()
    disp.mainloop()
