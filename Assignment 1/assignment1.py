# Initialize Global Variables
arr = None
rows = None
columns = None
winCondition = None
numMove = 0
up = None
down = None
left = None
right = None

# Assigns user input
def inputMode():
    # At first I did not want to put this in a function because it could've been
    # defined and assigned within the startgame or initialize function. However,
    # because the variables would be referenced in swapFunction and would need
    # to have been declared global anyways (for simplicity), I decided to place it
    # it a separate function to improve readability.
    global up
    global down
    global left
    global right
    up = input('Choose key for upwards direction: ')
    down = input('Choose key for downwards direction: ')
    left = input('Choose key for leftwards direction: ')
    right = input('Choose key for righwards direction: ')

# Initialize the board according to the game mode
def initialize(gameMode):
    global rows
    global columns
    global winCondition
    global arr
    inputMode()
    try:
        if gameMode == 1:
            rows, columns = (3, 3)
            winCondition = '12345678_'
        elif gameMode == 2:
            rows, columns = (4, 4)
            winCondition = '123456789101112131415_'   
        else:
            print('Invalid game mode. Exiting Game.')
        # Initializes the array with blank values
        arr = [[0 for i in range(columns)] for j in range(rows)]
    except:
        print('Error. Invalid. Please Try Again.')

# Sets default board values
def setDefault(gameMode):
    # At first I did not actually want to use a function for this,
    # but because I needed a way to reliably reset the game board
    # if the player decides to play the game again after winning,
    # I defined it as a function so that it could be called along with
    # the startGame function
    if gameMode == 1:    
        arr[0][0] = 1
        arr[0][1] = 2
        arr[0][2] = 3
        arr[1][0] = 4
        arr[1][1] = 5
        arr[1][2] = 6
        arr[2][0] = 7
        arr[2][1] = 8
        arr[2][2] = '_'
    elif gameMode == 2:
        arr[0][0] = 1
        arr[0][1] = 2
        arr[0][2] = 3
        arr[0][3] = 4
        arr[1][0] = 5
        arr[1][1] = 6
        arr[1][2] = 7
        arr[1][3] = 8
        arr[2][0] = 9
        arr[2][1] = 10
        arr[2][2] = 11
        arr[2][3] = 12
        arr[3][0] = 13
        arr[3][1] = 14
        arr[3][2] = 15
        arr[3][3] = '_'

# Function to refresh the play area, updates the values shown on screen
def refresh(gameMode):
    for rows in arr:
        if gameMode == 1:
            print('{:>4} {:>4} {:>4}'.format(*rows))
            print()
        elif gameMode == 2:
            print('{:>4} {:>4} {:>4} {:>4}'.format(*rows))
            print()

# Scrolls through the array and finds the coordinate of the value in the 2D array
def locateCoord(val):
    coord = [(indexRows, indexColumns)
            for indexRows, row in enumerate (arr)
            for indexColumns, column in enumerate (row)
            if val == column]
    return coord

# Executes the move (swap) function as well as checks if it is a legal move
def swapFunction(y, x,  direction):
    swap = arr[y][x]
    global numMove
    if direction == up:
        swapback = arr[y-1][x]
        if swapback == '_':
            arr[y-1][x] = swap
            arr[y][x] = swapback
            numMove += 1
            return
        else:
            print()
            print('Illegal. You can not move there.')
    elif direction == down:
        swapback = arr[y+1][x]
        if swapback == '_':
            arr[y+1][x] = swap
            arr[y][x] = swapback
            numMove += 1
            return
        else:
            print()
            print('Illegal. You can not move there.')
    elif direction == left:
        swapback = arr[y][x-1]
        if swapback == '_':
            arr[y][x-1] = swap
            arr[y][x] = swapback
            numMove += 1
            return
        else:
            print()
            print('Illegal. You can not move there.')
    elif direction == right:
        swapback = arr[y][x+1]
        if swapback == '_':
            arr[y][x+1] = swap
            arr[y][x] = swapback
            numMove += 1
            return
        else:
            print()
            print('You can not move there')
    else:
        print()
        print('Error. You did not enter a valid direction.')

# Function for accepting player input
def playerInput():
    tileCorrect = False
    while not tileCorrect:
        print('Select a tile to move')
        try:
            tileSelect = int(input('Move: '))
            # if tileSelect != 0: -> at first I used this because I used an int to represent
            # the blank space, now that the blank space is represented by a str, the try loop
            # will catch an attempted input of the blank space as well, simplifying the code 
            tileCoord = (locateCoord(tileSelect))
            tileCoord = tileCoord[0] # Bring the tuple out of the list
            if locateCoord(tileSelect):
                tileCorrect = True
        except:
            print('Error. Please input a number contained within the play area.')

    print('Select a direction to move')
    swapFunction(tileCoord[0], tileCoord[1], input('Direction: '))

# Game execution logic
def mainLogic(gameMode):
    print()
    refresh(gameMode)
    print('You have moved', numMove, 'times')
    print()
    playerInput()

# Game over logic
def gameOver():
    print('Congratulations, you have finished the game in', numMove, 'moves.')
    repeat = input('Would you like to play again? Y/N: ')
    if repeat == 'Y':
        startGame()
    elif repeat == 'y':
        startGame()
    elif repeat == 'N':
        raise SystemExit
    elif repeat == 'n':
        raise SystemExit
    else:
        print('Fatal input error. Exiting the game.')
        raise SystemExit

# Function to select gamemode and initialize play area
def startGame():
    gameOver = False
    modeInputOk = False
    print("Select a game mode")
    print("1. 3x3 Map (8 Tiles)")
    print("2. 4x4 Map (15 Tiles)")
    gameMode = input('Selected mode: ')
    while not modeInputOk:
        try:
            gameMode = int(gameMode)
            initialize(gameMode)
            setDefault(gameMode)
        except:
            print('Invalid game mode. Please try again.')
        modeInputOk = True
    while not gameOver:
        mainLogic(gameMode)
    else:
        gameOver()

startGame()