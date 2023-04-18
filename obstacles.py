# Create Obstacle class

class Obstacle:
    """
    TODO: DOCSTRING
    """
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


# create a class for each type of Obstacle
# TODO: POSSIBLY REMOVE THIS CLASS AND ADD THE OBSTACLES TO THE OBSTACLE CLASS
class Wall(Obstacle):
    """
    TODO: DOCSTRING
    """
    def __init__(self):
        super().__init__("Wall", 10)

# TODO: POSSIBLY REMOVE THIS CLASS AND ADD THE OBSTACLES TO THE OBSTACLE CLASS

class Trap(Obstacle):
    """
    TODO: DOCSTRING
    """
    def __init__(self):
        super().__init__("Trap", 20)
        