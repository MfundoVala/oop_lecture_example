"""
Player module containing player class and subclasses for creation of player
object.
"""
from .enemy import Enemy


class Player(Enemy):
    """
    Creates a player object with the necessary attributes and methods for
    player interaction.
    """

    def __init__(self, name, max_health, damage, player_type):
        super().__init__(name, max_health, damage)
        self.type = player_type

    def attack(self, obj):
        """
        Determines the result of player health remaining of after a collision
        with an enemy object.
        :return: True if player lives, False if player died.
        """
        obj.take_damage(self.damage)
        self.message = f"{self.name} deals {self.damage} damage to {obj.name}!"
        if obj.current_health <= 0:
            self.message += "\n" + f"{self.name} has defeated {obj.name}!"
            return True
        return False

    def is_dead(self):
        """Determine if player is dead."""
        return self.current_health <= 0
