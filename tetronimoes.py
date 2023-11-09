# tetronimo masks assuming they are centered at top left
#Also notes the necessary changes to the piece location required to actually work


def conv_xy_rowcol(x, y):
    '''Converts (row, col) to (x, y) and back
    Conversion is the same both ways'''
    return (y, x)

# Tuple version
def conv_xy_rowcol(coords):
    '''Converts (row, col) to (x, y) and back
    Conversion is the same both ways'''
    return (coords[1], coords[0])


# (x,y) transformation
# how you need to move the piece to align center with given location
TETRO_TRANS = {
    'O': (-1, 0),
    'Ih': (-2, 0),
    'Iv': (0, -2),
    'Ju': (-1, -1), 
    'Jd': (-1, 0), 
    'Jl':(-1, -1), 
    'Jr': (0, -1), 
    'Zh': (-1, 0), 
    'Zv': (0, -1), 
    'Sh': (-1, 0), 
    'Sv': (0, -1), 
    'Tu': (-1, -1), 
    'Tl': (-1, -1), 
    'Tr': (0, -1), 
    'Td': (-1, 0), 
    'Ld': (-1, 0), 
    'Ll': (-1, -1), 
    'Lr': (0, -1), 
    'Lu': (-1, -1)
}

# (0,0) at top left corner
# positive x is to the right
# x is a column measure
# positive y is to the bottom
# y is a row measure
TETRO_MASKS = {
    #Requires -1 to x
    "O": 
    [
        [1,1,0,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ],
    #Requires -2 to x
    "Ih": 
    [
        [1,1,1,1],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ],
    #Requires -2 to y
    "Iv": 
    [
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
    ],
    #Requires -1 to x and -1 to y
    "Ju":
    [
        [1,0,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to x
    "Jd":
    [
        [1,1,1,0],
        [0,0,1,0],
        [0,0,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to x and -1 to y
    "Jl":
    [
        [0,1,0,0],
        [0,1,0,0],
        [1,1,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to y
    "Jr":
    [
        [1,1,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to x
    "Zh":
    [
        [1,1,0,0],
        [0,1,1,0],
        [0,0,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to y
    "Zv":
    [
        [0,1,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to x
    "Sh":
    [
        [0,1,1,0],
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to y
    "Sv":
    [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to x and -1 to y
    "Tu":
    [
        [0,1,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to x and -1 to y
    "Tl":
    [
        [0,1,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,0,0,0],
    ],
    #requires -1 to y
    "Tr":
    [
        [1,0,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to x
    "Td":
    [
        [1,1,1,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to x
    "Ld":
    [
        [1,1,1,0],
        [1,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ],
    #REquires -1 to x and -1 to y
    "Ll":
    [
        [1,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to y
    "Lr":
    [
        [1,0,0,0],
        [1,0,0,0],
        [1,1,0,0],
        [0,0,0,0],
    ],
    #Requires -1 to x and -1 to y
    "Lu":
    [
        [0,0,1,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0],
    ],
}
