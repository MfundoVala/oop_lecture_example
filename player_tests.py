import unittest

from player import Player

class TestPlayer(unittest.TestCase):

    player = Player("mfundo", 100, 10, "Warrior")

    def test_player_name(self):
        """Test that player name is set correctly."""
        self.assertEqual(self.player.name, "mfundo")

    def test_player_max_health(self):
        """Test that player max health is set correctly."""
        self.assertEqual(self.player.max_health, 100)

    def test_player_dies_when_health_reaches_zero(self):
        """Test that player dies when health reaches zero."""
        self.player.current_health = 0
        self.assertTrue(self.player.is_dead())
    
if __name__ == "__main__":
    unittest.main()
        
    