import unittest
from unittest.mock import patch, MagicMock
from src.world import World

class WorldTestCase(unittest.TestCase):
    def setUp(self):
        self.world = World(10, None)
        self.world.grid = [[None for _ in range(10)] for _ in range(10)]
        self.world.player_position = (0, 0)
        self.world.player = MagicMock()

    @patch('builtins.print')
    def test_move_player_collision(self, mock_print):
        # Simulate collision with a wall
        self.world.move_player("w")

        # Assert that the player position remains the same
        self.assertEqual(self.world.player_position, (0, 0))

        # Assert that the print function was called with the appropriate message
        mock_print.assert_called_with("You hit a Wall and take 10 damage!")

        # Assert that the player's take_damage method was called
        self.world.player.take_damage.assert_called_with(10)

    @patch('builtins.print')
    def test_move_player_no_collision(self, mock_print):
        # Simulate no collision
        self.world.grid[1][0] = None

        # Move player down
        self.world.move_player("s")

        # Assert that the player position has been updated
        self.assertEqual(self.world.player_position, (1, 0))

        # Assert that the grid reflects the new player position
        self.assertEqual(self.world.grid[0][0], None)
        self.assertEqual(self.world.grid[1][0], self.world.player)

        # Assert that appropriate messages were printed
        mock_print.assert_called_with("You move into the empty space.")

    @patch('builtins.print')
    def test_move_player_enemy_collision(self, mock_print):
        # Simulate collision with an enemy
        enemy = MagicMock()
        self.world.grid[1][0] = enemy

        # Move player down
        self.world.move_player("s")

        # Assert that the enemy's attack method was called
        enemy.attack.assert_called_with(self.world.player)

        # Assert that the appropriate message was printed
        self.assertEqual(mock_print.call_args[0][0], self.world.player.message)

        # Assert that the enemy was removed from the grid if defeated
        self.assertEqual(self.world.grid[1][0], None)

    @patch('builtins.print')
    def test_move_player_exit_collision(self, mock_print):
        # Simulate collision with the exit
        exit_obj = MagicMock()
        self.world.grid[1][0] = exit_obj

        # Move player down
        self.world.move_player("s")

        # Assert that the appropriate message was printed
        self.assertEqual(mock_print.call_args[0][0], exit_obj.message)

        # Assert that the sys.exit function was called
        self.assertTrue(self.world.player.is_dead())

if __name__ == '__main__':
    unittest.main()
