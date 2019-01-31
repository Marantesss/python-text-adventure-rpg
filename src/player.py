import random
import items, world

class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock()]
        self.hp = 100
        self.location_x, self.location_y = world.startingPosition
        self.victory = False

    def isAlive(self):
        return self.hp > 0

    '''
    We’re looking for a method in a class. For example, if action is a
    MoveNorth action, then we know that its internal method is
    player.moveNorth. The __name__ of that method is “moveNorth”.
    Then getattr() finds the moveNorth method inside the player class
    and stores that method as the object actionMethod.
    '''
    def doAction(self, action, **kwargs):
        actionMethod = getattr(self, action.method.__name__)
        if actionMethod:
            actionMethod(**kwargs)

    def printInventory(self):
        for item in self.inventory:
            print(item, '\n')
        
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tileExists(self.location_x, self.location_y).introText())
    
    def moveNorth(self):
        self.move(dx=0, dy=-1)
    
    def moveSouth(self):
        self.move(dx=0, dy=1)
    
    def moveEast(self):
        self.move(dx=1, dy=0)
    
    def moveWest(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        bestWeapon = None
        maxDamage = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon): # ee if the item is a Weapon
                if i.damage > maxDamage:
                    maxDamage = i.damage
                    bestWeapon = i
        
        print("You use {} against {}!".format(bestWeapon.name, enemy.name))
        enemy.hp -= bestWeapon.damage
        if not enemy.isAlive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{}'s HP is {}!".format(enemy.name, enemy.hp))

    def flee(self, tile):
        "Moves the player randomly to an adjacent tile"
        availableMoves = tile.adjacentMoves()
        r = random.randint(0, len(availableMoves) - 1)
        self.doAction(availableMoves[r])
