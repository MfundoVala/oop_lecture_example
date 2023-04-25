from player import Player

class Gnome(Player):
    

    def __init__(self, name):
        super().__init__(name, 50, 50, "Gnome")
        self.prefix = name[0]