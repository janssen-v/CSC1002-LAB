# The Snake Game
import turtle as t

# Snake unit
snake = t.Turtle()
snake.color('black')
snake.shape('square')
snake.penup()
snake.speed(0)

# Refresh Tick
speed = 1

# Snake turns
def leftTurn():
    snake.left(90)

def rightTurn():
    snake.right(90)

def speedUp():
    global speed
    speed += 1

# Keybinds
t.listen()
t.onkey(leftTurn, 'Left')
t.onkey(rightTurn, 'Right')
t.onkey(speedUp, 'Up')

# Collision Detector

while True:
    snake.forward(speed)