"""
Enemy module containing Enemy class and subclasses for creation of Enemy
objects.
"""


class Enemy:
    """
    Creates a enemy object with the necessary attributes and methods for
    enemy interaction.
    """
    def __init__(self, name, max_health, damage):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.damage = damage
        self.message = ""

    def attack(self, player):
        """
        Applies a damage value to player's health after a collision
        with an enemy object.
        """
        damage = self.damage
        player.current_health -= damage
        self.message = f"The {self.name} deals {damage} damage to {player.name}!"
