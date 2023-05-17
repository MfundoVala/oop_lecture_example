import unittest
from unittest.mock import patch, MagicMock
from world import World
from player import Player

class WorldTestCase(unittest.TestCase):
    def setUp(self):
        self.world = World(10, None)
        self.world.grid = [[None for _ in range(10)] for _ in range(10)]
        self.world.player_position = (0, 0)
        self.world.player = Player("mfundo", 100, 10, "Warrior")

    @patch('builtins.print')
    def test_move_player_collision(self, mock_print):
        # Simulate move
        self.world.move_player("w")

        # Assert that the player position moves
        self.assertEqual(self.world.player_position, (0, 1))

        # Assert that the print function was called with the appropriate message
        mock_print.assert_called_with("You move into the empty space.")


if __name__ == '__main__':
    unittest.main()
