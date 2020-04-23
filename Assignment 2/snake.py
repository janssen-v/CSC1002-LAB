# The Snake Game
import turtle as t

# Snake unit
snake = t.Turtle()
snake.color('black')
snake.shape('square')
snake.penup()
snake.speed(0)

# Snake turns
def leftTurn():
    snake.left(45)

def rightTurn():
    snake.right(45)

# Keybinds
t.listen()
t.onkey(leftTurn, 'Left')
t.onkey(rightTurn, 'Right')