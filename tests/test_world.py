"""Test file for world.py."""
import unittest

from src.world import World
from src.custom_errors import WorldFullError


class WorldTest(unittest.TestCase):
    """Class for world tests."""

    def test_world_full_fails(self):
        """Failing Test that world full error is raised when world is full."""

        # Given / Arrange
        world = World(10, None)

        # Assert
        with self.assertRaises(WorldFullError):
            # When / Act
            world.add_objects(200,'Goblin')

    


if __name__ == "__main__":
    unittest.main()
