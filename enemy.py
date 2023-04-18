"""
TODO: Add a description of this file
"""
class Enemy:
    """
    TODO: Add a description of this class
    """
    def __init__(self, name, max_health, damage):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.damage = damage
        self.message = ""
        self.type = "Enemy"

    def attack(self, player):
        """
        TODO: Add a description of this method
        """
        damage = self.damage
        player.current_health -= damage
        self.message = f"The {self.name} deals {damage} damage to {player.name}!"


# create a class for each type of Enemy 
# TODO: POSSIBLY REMOVE THIS CLASS AND ADD THE ENEMIES TO THE ENEMY CLASS

class Goblin(Enemy):
    """
    TODO: Add a description of this class
    """
    def __init__(self):
        super().__init__("Goblin", 20, 50)

# TODO: POSSIBLY REMOVE THIS CLASS AND ADD THE ENEMIES TO THE ENEMY CLASS

class Orc(Enemy):
    """
    TODO: Add a description of this class
    """
    def __init__(self):
        super().__init__("Orc", 30, 10)
