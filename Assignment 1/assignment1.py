# Define input

# Initialize Global Variables
rows = None
columns = None
gameOver = False
legalMoves = None
winCondition = None
numMove = 0
up = None
down = None
left = None
right = None

# Defines user input
def inputMode():
    global up
    global down
    global left
    global right
    up = input('Choose key for upwards direction: ')
    down = input('Choose key for downwards direction: ')
    left = input('Choose key for leftwards direction: ')
    right = input('Choose key for righwards direction: ')
# Defines the game mode
def initialize(gameMode):
    global rows
    global columns
    global legalMoves
    global winCondition
    inputMode()
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
        print('    '.join(map(str, row))) # Only str objects can be joined,
        print()                           # so output is mapped to string

# Sets default board values
arr[0][0] = 1
arr[0][1] = 2
arr[0][2] = 3
arr[1][0] = 4
arr[1][1] = 5
arr[1][2] = 6
arr[2][0] = 7
arr[2][1] = 8
arr[2][2] = 0

# Scrolls through the array and finds the coordinate of the value in the 2D array
def locateCoord(val):
    coord = [(indexRows, indexColumns)
            for indexRows, row in enumerate (arr)
            for indexColumns, column in enumerate (row)
            if val == column]
    return coord

# Executes the move (swap) function as well as check if it is a legal move
def swapFunction(y, x,  direction):
    swap = arr[y][x]
    if direction == up:
        swapback = arr[y-1][x]
        if swapback == 0:
            arr[y-1][x] = swap
            arr[y][x] = swapback
            numMove =+ 1
            return
        else:
            print()
            print('Illegal. You can not move there.')
    elif direction == down:
        swapback = arr[y+1][x]
        if swapback == 0:
            arr[y+1][x] = swap
            arr[y][x] = swapback
            numMove =+ 1
            return
        else:
            print()
            print('Illegal. You can not move there.')
    elif direction == left:
        swapback = arr[y][x-1]
        if swapback == 0:
            arr[y][x-1] = swap
            arr[y][x] = swapback
            numMove =+ 1
            return
        else:
            print()
            print('Illegal. You can not move there.')
    elif direction == right:
        swapback = arr[y][x+1]
        if swapback == 0:
            arr[y][x+1] = swap
            arr[y][x] = swapback
            numMove =+ 1
            return
        else:
            print()
            print('You can not move there')
    else:
        print()
        print('Error. You did not enter a valid direction.')

# Player selects a block or tile to move
def playerInput():
    global numMove
    tileCorrect = False
    while not tileCorrect:
        print('Select a tile to move')
        tileSelect = int(input('Move: '))
        if tileSelect != 0:
            tileCoord = (locateCoord(tileSelect))
            tileCoord = tileCoord[0] # Bring the tuple out of the list
            if locateCoord(tileSelect):
                tileCorrect = True
            else: print('Invalid selection.')
        else:
            print('Error. You can not move the blank space.')
    print('Select a direction to move')
    swapFunction(tileCoord[0], tileCoord[1], input('Direction: '))
    

# Refreshes screen after player input
while not gameOver:
    print('////////////')
    print()
    refresh()
    print('////////////')
    print('You have moved', numMove, 'times')
    print()
    playerInput()
else:
    print('Congratulations, you have finished the game in', numMove, 'moves.')
    repeat = input('Would you like to play again? Y/N: ')
    if repeat == 'yes':
        startGame()
