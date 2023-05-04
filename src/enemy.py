"""
Enemy module containing Enemy class and subclasses for creation of Enemy
objects.
"""
# pylint: disable=import-error
from .obstacles import Obstacle


class Enemy(Obstacle):
    """
    Creates a enemy object with the necessary attributes and methods for
    enemy interaction.
    """
    def __init__(self, name, max_health, damage):
        super().__init__(name, damage)
        self.max_health = max_health
        self.current_health = max_health
        self.message = ""

    def attack(self, obj):
        """
        Applies a damage value to player's health after a collision
        with an enemy object.
        """
        damage = self.damage
        obj.current_health -= damage
        self.message = f"The {self.name} deals {damage} damage to {obj.name}!"

    def take_damage(self, damage_amount):
        """Reduces objects health by amount given."""
        self.current_health -= damage_amount
