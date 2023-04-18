# create ENEMY class
class Enemy:
    def __init__(self, name, max_health, damage):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.damage = damage
        self.message = ""
        self.type = "Enemy"

    def attack(self, player):
        damage = self.damage
        player.current_health -= damage
        self.message = f"The {self.name} deals {damage} damage to {player.name}!"


# create a class for each type of Enemy
class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 20, 50)


class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 30, 10)