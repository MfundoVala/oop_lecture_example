# Create Obstacle class
class Obstacle:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


# create a class for each type of Obstacle
class Wall(Obstacle):
    def __init__(self):
        super().__init__("Wall", 10)


class Trap(Obstacle):
    def __init__(self):
        super().__init__("Trap", 20)