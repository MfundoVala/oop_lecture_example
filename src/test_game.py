import unittest
from unittest.mock import patch, MagicMock
from world import World

class WorldTestCase(unittest.TestCase):
    
    @patch("player.Player")
    def setUp(self, player):
        # Arrange
        self.world = World(10, None)
        self.world.player = player
        self.world.player.player_position = (0, 0)
        self.world.player.current_health = 100
        self.pick_up = MagicMock(value=0)
        
    def set_pick_up_name(self, new_name):
        self.pick_up.name = new_name
        
    def set_pick_up_value(self, new_value):
        self.pick_up.value = new_value
    
    def test_move_player_into_an_empty_space(self):
        # Act
        self.world.move_player("d")
        # Assert that the player position moves
        self.assertEqual(self.world.player.player_position, (0, 1))
        
    def test_player_moves_over_health_pickup_and_health_increases_by_fifty(self):
        # Arrange
        self.set_pick_up_name("Health")
        self.set_pick_up_value(50)
        self.world.grid[0][1] = self.pick_up
        # Act
        self.world.move_player("d")
        # Assert
        self.assertEqual(self.world.player.current_health, 150)
        
    def test_player_moves_over_health_pickup_and_health_increases_by_hundred(self):
        # Arrange
        self.set_pick_up_name("Health")
        self.set_pick_up_value(100)
        self.world.grid[0][1] = self.pick_up
        # Act
        self.world.move_player("d")
        # Assert
        self.assertEqual(self.world.player.current_health, 200)
        


if __name__ == '__main__':
    unittest.main()
