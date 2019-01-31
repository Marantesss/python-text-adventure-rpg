class Enemy():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self. damage = damage

    def isAlive(self):
        return self.hp > 0

class Mudcrab(Enemy):
    def __init__(self):
        super().__init__(name = "Mudcrab", hp = 5, damage = 2)

class Draugr(Enemy):
    def __init__(self):
        super().__init__(name = "Draugr", hp = 10, damage = 5)

class FrostTroll(Enemy):
    def __init__(self):
        super().__init__(name = "Frost Troll", hp = 30, damage = 15)
