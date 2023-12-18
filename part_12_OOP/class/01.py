class Human:
    def __init__(self, health: int):
        self.health = health

    def attack(self):
        print(f"I DONT KNOW WHO TO ATTACK")


class Warrior(Human):
    def __init__(self, health: int, defense: float):
        super().__init__(health)
        self.defense = defense

    def attack(self, victim):
        print(f"Warrior attacked Barbarian. health: {victim.health - victim.damage} ")


class Barbarian(Human):
    def __init__(self, health: int, damage: int):
        super().__init__(health)
        self.damage = damage

    def attack(self, victim):
        print(f"Barbarian attacked Warrior. health: {victim.health} ")


class Person(Human):
    pass


person = Person(250)
person.attack()

warrior = Warrior(50, 20.4)
barbarian = Barbarian(100, 20)

warrior.attack(barbarian)
barbarian.attack(warrior)
