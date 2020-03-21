# Define input

# Initialize Global Variables
rows = None
columns = None
gameOver = False
legalMoves = None
winCondition = None
up = None
down = None
left = None
right = None

def inputMode():
    global up
    global down
    global left
    global right
    up = input('Choose key for upwards direction: ')
    down = input('Choose key for downwards direction: ')
    left = input('Choose key for leftwards direction: ')
    right = input('Choose key for righwards direction: ')

def initialize(gameMode):
    global rows
    global columns
    global legalMoves
    global winCondition
    if gameMode == 1:
        rows, columns = (3, 3)
        legalMoves = [1, 2, 3, 4, 5, 6, 7, 8]
        winCondition = 123456780
    elif gameMode == 2:
        rows, columns = (4, 4)
        legalMoves = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0]
        winCondition = 12345678910111213140   
    else:
        print('Invalid game mode. Exiting Game.')

# Starts the game
def startGame():
    print("Select a game mode")
    print("1. 3x3 Map (8 Tiles)")
    print("2. 4x4 Map (15 Tiles)")
    initialize(int(input('Selected mode: ')))

startGame()

# Initializes the array with blank values
arr = [[0 for i in range(columns)] for j in range(rows)]

# Refreshes the play area and updates the values shown on screen
def refresh():
    for row in arr:
# Only str objects can be joined, so output is mapped to string
        print('    '.join(map(str, row)))
        print()

# Sets default board values
arr[0][0] = '1'
arr[0][1] = '2'
arr[0][2] = '3'
arr[1][0] = '4'
arr[1][1] = '5'
arr[1][2] = '6'
arr[2][0] = '7'
arr[2][1] = '8'
arr[2][2] = '_'

def locateCoord(val):
# Scrolls through the array and finds the coordinate of the value
    coord = [(indexRows, indexColumns)
            for indexRows, row in enumerate (arr)
            for indexColumns, column in enumerate (row)
            if val == column]
    return coord

def swapDirection(tile, direction):
    swap = arr[tile]
    direction = 'w', 'a', 's', 'd'

# Player selects a block or tile to move
def playerInput():
    print('Select a tile to move')
    tileSelect = int(input('Move: '))
    tileCoord = (locateCoord(tileSelect))
    print(tileCoord)
    print('Select a direction to move')
    swapDirection = (tileCoord, input('Direction: '))

# Refreshes screen after player input
while not gameOver:
    refresh()
    print(arr)
    playerInput()