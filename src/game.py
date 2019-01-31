import world
from player import Player

def play():
    world.loadTiles()
    player = Player()
    while player.isAlive() and not player.victory:
        room = world.tileExists(player.location_x, player.location_y)
        room.modifyPlayer(player)
        # Check again since the room could have changed the player's state
        if player.isAlive() and not player.victory:
            print("---------------")
            print("Choose an action:\n")
            availableActions = room.availableActions()
            for action in availableActions:
                print(action)
            actionInput = input('Action: ')
            for action in availableActions:
                if actionInput == action.hotkey:
                    player.doAction(action, **action.kwargs)
                    break

if __name__ == "__main__":
    play()