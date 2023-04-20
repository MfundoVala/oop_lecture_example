"""
Player module containing player class and subclasses for creation of player
object.
"""


class Player:
    """
    Creates a player object with the necessary attributes and methods for
    player interaction.
    """

    def __init__(self, name, max_health, damage, player_type):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.damage = damage
        self.message = ""
        self.type = player_type

    def attack(self, enemy):
        """
        Determines the result of player health remaining of after a collision
        with an enemy object.
        :return: True if player lives, False if player died.
        """
        damage = self.damage
        enemy.current_health -= damage
        self.message = f"{self.name} deals {damage} damage to {enemy.name}!"
        if enemy.current_health <= 0:
            self.message += "\n" + f"{self.name} has defeated {enemy.name}!"
            return True
        return False
