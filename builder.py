class Unit:
    def __init__(self):
        self.type = None
        self.health = 0
        self.armor = 0
        self.weapon = None
        self.fraction = None
    def __str__(self):
        return f"Тип юнита: {self.type}, здоровье: {self.health}, броня: {self.armor}, оружие: {self.weapon}, фракция: {self.fraction}"


class CreateUnit:
    def __init__(self):
        self.unit = Unit()
    def set_type(self, type: str):
        self.unit.type = type
        return self
    def set_health(self, health: int):
        self.unit.health = health
        return self
    def set_armor(self, armor: int):
        self.unit.armor = armor
        return self
    def set_weapon(self, weapon: str):
        self.unit.weapon = weapon
        return self
    def set_fraction(self, fraction: str):
        self.unit.fraction = fraction
        return self
    def create(self):
        return self.unit

def main():
    unit = CreateUnit().set_type("archer").set_health(78).set_armor(30).set_weapon("banana").set_fraction("mordor").create()
    print(unit)

if __name__ == "__main__":
    main()
