# Define input

# Initialize Global Variables
rows = None
columns = None
arr = None

def initialize(gameMode):
    global rows
    global columns
    if gameMode == 8:
        rows, columns = (3, 3)
    elif gameMode == 15:
        rows, columns = (4, 4)
    else:
        print('Invalid game mode. Exiting Game.')

# Assigns default values for each point
arr = [[0 for i in range(columns)] for j in range(rows)] 

def refresh():
# Refreshes the play area and updates the values shown on screen
    for row in arr:
        # Only str objects can be joined, so output is mapped to string
        print('    '.join(map(str, row)))
        print()

# Defines the values
arr[0][0] = 1
arr[0][2] = 2
