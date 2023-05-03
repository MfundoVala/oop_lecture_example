"""
Player tests.
"""

import unittest
from unittest.mock import patch

from player import Player

class TestPlayer(unittest.TestCase):
    """Class for player tests."""

    # Given / Arrange
    name = "mfundo"
    max_health = 100
    attack = 10
    player_type = "Warrior"

    player = Player(name, max_health, attack, player_type)
    player_two = Player("mfundo", 100, 10, "Warrior")

    def test_player_name(self):
        """Test that player name is set correctly."""

        # Assert
        self.assertEqual(self.player.name, "mfundo")

    def test_player_max_health(self):
        """Test that player max health is set correctly."""

        # Assert
        self.assertEqual(self.player.max_health, 100)

    def test_player_dies_when_health_reaches_zero(self):
        """Test that player dies when health reaches zero."""

        # When / Act
        self.player.current_health = 0

        # Then / Assert
        self.assertTrue(self.player.is_dead())

    def test_player_takes_damage_from_obstacle(self):
        """Test that player takes damage from obstacle."""

        # Given / Arrange
        damage = 10

        # When / Act
        self.player_two.take_damage(damage)

        # Then / Assert
        self.assertEqual(self.player_two.current_health, 90)


if __name__ == "__main__":
    unittest.main()
  