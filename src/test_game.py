import unittest
from unittest.mock import patch, MagicMock
from world import World
import player

class WorldTestCase(unittest.TestCase):
    
    @patch("player.Player")
    def setUp(self, player):
        # Arrange
        self.world = World(10, None)
        self.world.player = player
        self.world.player.player_position = (0, 0)
        self.world.player.current_health = 100

    
    def test_move_player_into_an_empty_space(self):
        # Act
        self.world.move_player("d")
        # Assert that the player position moves
        self.assertEqual(self.world.player.player_position, (0, 1))
        
    def test_player_moves_over_health_pickup_and_health_increases_by_fifty(self):
        health_pick_up = MagicMock(value = 50)
        health_pick_up.name= "health"
        self.world.grid[0][1] = health_pick_up
        self.world.move_player("d")
        self.assertEqual(self.world.player.current_health, 150)
        
    def test_player_moves_over_health_pickup_and_health_increases_by_hundred(self):
        health_pick_up = MagicMock(value = 100)
        health_pick_up.name= "health"
        self.world.grid[0][1] = health_pick_up
        self.world.move_player("d")
        self.assertEqual(self.world.player.current_health, 200)


if __name__ == '__main__':
    unittest.main()
