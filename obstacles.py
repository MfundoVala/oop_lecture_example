"""Obstacles module containing obstacle class definition."""


class Obstacle:
    """
    Creates an obstacle object taht collides with player and deals damage.
    """
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.prefix = self.name[0]
