import items, enemies, actions, world

# MapTile is an abstract base class because
# we don’t want to create any instances of it
class MapTile():
    "The base class for a tile within the world space"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def introText(self):
        "Information to be displayed when the player moves into this tile"
        raise NotImplementedError()
 
    def modifyPlayer(self, player):
        "Process actions that change the state of the player."
        raise NotImplementedError()

    def adjacentMoves(self):
        "Returns all move actions for adjacent tiles"
        moves = []
        if world.tileExists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tileExists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        if world.tileExists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tileExists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        return moves

    def availableActions(self):
        "Returns all available actions in this room."
        availableActions = self.adjacentMoves()
        availableActions.append(actions.ViewInventory())
        return availableActions
            
class StartingRoom(MapTile):
    def introText(self):
        return """You've awaken and find yourself lost inside a cave with a flcikering torch on the wall.
        You grab it not knowing what awaits you. You also can make out four paths,
        each equally dark and mysterious."""

    def modifyPlayer(self, player):
        # This room has no action on the player
        pass # Tells the interpreter to do nothing

class EmptyCavePath(MapTile):
    def introText(self):
        return "Another unremarkable part of the cave. You must forge onwards."
 
    def modifyPlayer(self, player):
        #Room has no action on player
        pass

class LeaveCaveRoom(MapTile):
    def introText(self):
        return """
        You see a bright light in the distance...
        It grows as you get closer! It's sunlight
        
        Victory is yours! :)
        """

    def modifyPlayer(self, player):
        player.victory = True

### Loot Rooms ###

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def modifyPlayer(self, player):
        self.addLoot(player)

    def addLoot(self, player):
        player.inventory.append(self.item)

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def introText(self):
        return "You notice a sharp object in the corner. It's a dagger! You pick it up."

class FindGreatswordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def introText(self):
        return "You fell the power calling to you. It's the Greatsword! You pick it up and feel more powerfull than ever."

class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))

    def introText(self):
        return "You notice something shiny. It's a gold piece! You pick it up."

### Enemy Rooms ###

class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modifyPlayer(self, player):
        if self.enemy.isAlive():
            player.hp -= self.enemy.damage
            print("Enemy does {} damage. You currently have {} HP remaining!".format(self.enemy.damage, player.hp))

    '''
    We need to override this functions because
    in enemy rooms we can only flee or fight
    '''
    def availableActions(self):
        if self.enemy.isAlive():
            return [actions.Flee(tile = self), actions.Attack(enemy = self.enemy)]
        else:
            return self.adjacentMoves()

class MudcrabRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Mudcrab())

    def introText(self):
        if self.enemy.isAlive():
            return "You notice a crab-like creature as he runs towards you!"
        else:
            return "Looks like this crab won't be bothering anyone else."

class DraugrRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Draugr())

    def introText(self):
        if self.enemy.isAlive():
            return "An ancient looking corpse appears to be more alive then dead!"
        else:
            return "The corpse of the undead lies on the ground."

class FrostTrollRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.FrostTroll())

    def introText(self):
        if self.enemy.isAlive():
            return "A bone chilling wind blows on your face and you notice a bear-like creature in the corner of the room!"
        else:
            return "Even though the creature is dead, the cold still lingers."

class SkeaverPitRoom(MapTile):
    def introText(self):
        return """
        You have fallen into a pit of starving skeavers!
        You have died!
        """

    def modifyPlayer(self, player):
        player.hp = 0