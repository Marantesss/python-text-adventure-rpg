class Item():
    "Base class for items"
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n----- Description -----\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    "Everyone loves treasure :)"
    def __init__(self, amount):
        self.amount = amount
        # We could also have called Item.__init__(self, name = "Gold", ...)
        # Super().__init__() is utomatically replaced by a call to the superclasses method
        super().__init__(name = "Gold",
                         description = "A shiny coin with {} stamped on the front. Doesn't taste very good.".format(self.amount),
                         value = self.amount)

        # If a subclass doesn’t define its own __str__ method, the superclass method will be used in its place

class Weapon(Item):
    "We need some weapons to kill frost trolls"
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n----- Description -----\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)

class Rock(Weapon):
    def __init__(self):
        super().__init__(name = "Rock",
                         description = "Just a small rock, you won't be slaying dragons anytime soon.",
                         value = 1,
                         damage = 5)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name = "Dagger",
                         description = "It's a bit rusty, but it sure beats using your fists.",
                         value = 5,
                         damage = 10)

class Greatsword(Weapon):
    def __init__(self):
        super().__init__(name = "Greatsword",
                         description = "Used by a famous dragon hunter, it still has some of its magical powers.",
                         value = 40,
                         damage = 20)
