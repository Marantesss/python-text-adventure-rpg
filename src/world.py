import game

_world = {}
currentPosition = [0, 0]
numCols = 0
numRows = 0

def tileExists(x, y):
    """Returns the tile at the given coordinates or None if there is no tile.
    
    :param x: the x-coordinate in the worldspace
    :param y: the y-coordinate in the worldspace
    :return: the tile at the given coordinates or None if there is no tile
    """
    return _world.get((x, y))

def loadTiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
    global numCols
    numCols = len(rows[0].split('\t')) # Assumes all rows contain the same number of tabs
    global numRows
    numRows = len(rows)
    for y in range(numRows):
        cols = rows[y].split('\t')
        for x in range(numCols):
            tileName = cols[x].replace('\n', '')
            if tileName == "StartingRoom":
                global currentPosition
                currentPosition = [x, y]
            _world[(x, y)] = None if tileName == '' else getattr(__import__('tiles'), tileName) (x, y)

def drawBoard():
    for y in range(numRows):
        for x in range(numCols):
            if currentPosition == [x, y]:
                print(" O ", end = "")
            elif tileExists(x, y):
                print(" X ", end = "")
            else:
                print("   ", end = "")
        print()

