from database_manager import DatabaseManager
import random
from Player import *
from enemy import *
from obstacles import *

class Exit:
    def __init__(self, message):
        self.message = message


class World:
    size = 0
    player = None
    db = DatabaseManager()

    def __init__(self, size):
        self.size = size
        self.grid = [ [ None for _ in range(size) ] for _ in range(size) ]
        self.player_position = (0, 0)

    # print the map from the 2d array grid values
    def print_map(self):
        for row in self.grid:
            for cell in row:
                if cell is None:
                    print(".", end="")
                elif isinstance(cell, Player):
                    print("P", end="")
                elif isinstance(cell, Obstacle):
                    print("O", end="")
                elif isinstance(cell, Enemy):
                    print("E", end="")
                elif isinstance(cell, Exit):
                    print("X", end="")
            print()
        self.store_grid_to_file()
        if not self.player is None:
            self.store_player_data()

    def store_player_data(self):
        self.db.save_player_data("Player", self.player_position, self.player.name, self.player.max_health,
                                  self.player.current_health, self.player.damage)

    def store_grid_to_file(self):
        with open("grid_save.txt", "w") as file:
            for row in self.grid:
                for cell in row:
                    if cell is None:
                        file.write(".")
                    elif isinstance(cell, Player):
                        file.write("P")
                    elif isinstance(cell, Obstacle):
                        file.write("O")
                    elif isinstance(cell, Enemy):
                        file.write("E")
                    elif isinstance(cell, Exit):
                        file.write("X")
                file.write("\n")

    def get_stored_world(self):
        with open("grid_save.txt", "r") as file:
            data = file.readlines()
            for x, line in enumerate(data):
                for y in range(len(line)):
                    if line[y] == "E":
                        self.grid[x][y] = random.choice([Goblin(), Orc()])
                    elif line[y] == "O":
                        self.grid[x][y] = random.choice([Wall(), Trap()])
                    elif line[y] == "X":
                        self.grid[x][y] = Exit("Goodbye")
                    elif line[y] == "P":
                        player_data = self.db.retrieve_player_data()
                        self.grid[x][y] = self.player
                        self.player_position = (y, x)
                        print(player_data)

    def move_player(self, direction):
        output = """Game start!"""

        x, y = self.player_position
        if direction == "w" or direction == "up":
            y -= 1
        elif direction == "s" or direction == "down":
            y += 1
        elif direction == "a" or direction == "left":
            x -= 1
        elif direction == "d" or direction == "right":
            x += 1

        if x < 0 or x >= self.size or y < 0 or y >= self.size:
            print("You hit a wall!")
            return

        cell = self.grid[y][x]
        
        if cell is None:
            output = "You move into the empty space."

        elif isinstance(cell, Obstacle):
            damage = cell.damage
            output = f"You hit a {cell.name} and take {damage} damage!"
            self.player.current_health -= damage
            if self.player.current_health <= 0:
                output = "You have died."
                exit()
        elif isinstance(cell, Enemy):
            enemy_defeated = self.player.attack(cell)
            output = \
                self.player.message
            if enemy_defeated:
                self.grid[y][x] = None
        elif isinstance(cell, Exit):
            print(cell.message)
            exit()

        self.grid[self.player_position[1]][self.player_position[0]] = None
        self.player_position = (x, y)
        self.grid[y][x] = self.player

        self.print_map()

        print(output)

    def save(self):
        # save
    
        pass
