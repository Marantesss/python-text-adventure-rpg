_world = {}
startingPosition = (0, 0)

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
    x_max = len(rows[0].split('\t')) # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tileName = cols[x].replace('\n', '')
            if tileName == "StartingRoom":
                global startingPosition
                startingPosition = (x, y)
            _world[(x, y)] = None if tileName == '' else getattr(__import__('tiles'), tileName) (x, y)

