"""Test enemy class."""
import unittest

from enemy import Enemy
from player import Player

class EnemyTest(unittest.TestCase):
    """Class for enemy tests."""

    # Given / Arrange
    enemy_name = "Goblin"
    enemy_max_health = 100
    enemy_attack = 10
    enemy = Enemy(enemy_name, enemy_max_health, enemy_attack)

    # Given / Arrange
    player_name = "mfundo"
    player_max_health = 100
    player_attack = 10
    player_type = "Warrior"
    player = Player(player_name, player_max_health, player_attack, player_type)

    def test_enemy_name(self):
        """Test that enemy name is set correctly."""

        # Assert
        self.assertEqual(self.enemy.name, "Goblin")

    def test_enemy_take_damage(self):
        """Test that enemy takes damage."""

        # When / Act
        self.enemy.take_damage(10)

        # Then / Assert
        self.assertEqual(self.enemy.current_health, 90)

    def test_enemy_attack(self):
        """Test that enemy takes damage when attacking."""

        # When / Act
        self.enemy.attack(self.player)

        # Then / Assert
        self.assertEqual(self.player.current_health, 90)
        self.assertEqual(self.enemy.message, "The Goblin deals 10 damage to mfundo!")




if __name__ == "__main__":
    unittest.main()