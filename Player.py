# create Player class
class Player:
    
    def __init__(self, name, max_health, damage):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.damage = damage
        self.message = ""
        self.type = "Player"

    def attack(self, enemy):
        damage = self.damage
        enemy.current_health -= damage
        self.message = f"{self.name} deals {damage} damage to {enemy.name}!"
        if enemy.current_health <= 0:
            self.message += "\n" + f"{self.name} has defeated {enemy.name}!"
            return True
        return False


# create a class for each type of Player
class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, 100, 10)


class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, 20, 20)