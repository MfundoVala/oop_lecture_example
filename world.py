"""
This module contains the World class, which is used 
to create a world for the player to explore.
"""
import random
import sys
from player import Player
from obstacles import Obstacle
from enemy import Enemy


class Exit:
    """
    Creates an exit object for detecting if player finished game.
    """
    def __init__(self, message):
        self.message = message


class World:
    """
    Creates a world object responsible for providing output to player,
    detecting player movement and storing player data.
    """
    size = 0
    player = None

    def __init__(self, size, database):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size) ]
        self.player_position = (0, 0)
        self.database = database

    # print the map from the 2d array grid values
    def print_map(self):
        """
        Print world map to terminal.
        """
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
        if self.player is not None:
            self.store_player_data()

    def store_player_data(self):
        """
        Store player data to database through DatabaseManager.
        """
        self.database.save_player_data(self.player, self.player_position)

    def store_grid_to_file(self):
        """
        Stores a copy of the world to a text file to recall for world
        restoration.
        """
        with open("grid_save.txt", "w", encoding="utf-8") as file:
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
        """
        Retrieve required data to restore previous world.
        """
        with open("grid_save.txt", "r", encoding="utf-8") as file:
            data = file.readlines()
            for x_position, line in enumerate(data):
                for y_position, value in enumerate(line):
                    if value == "E":
                        self.grid[x_position][y_position] = random.choice([Enemy("Goblin", 20, 50),
                                                                           Enemy("Orc", 30, 10)])
                    elif value == "O":
                        self.grid[x_position][y_position] = random.choice([Obstacle("Wall", 10),
                                                                           Obstacle("Trap", 20)])
                    elif value == "X":
                        self.grid[x_position][y_position] = Exit("Goodbye")
                    elif value == "P":
                        player_data = self.database.retrieve_player_data()
                        self.grid[x_position][y_position] = self.player
                        self.player_position = (y_position, x_position)
                        print(player_data)

    def move_player(self, direction):
        """
        Move player to given direction and detect if a collision has occurred.
        :param direction: Direction player moves in.
        """
        output = """Game start!"""

        x_position, y_position = self.player_position
        if direction in ("w", "up"):
            y_position -= 1
        elif direction in ("s", "down"):
            y_position += 1
        elif direction in ("a", "left"):
            x_position -= 1
        elif direction in ("d", "right"):
            x_position += 1

        if x_position < 0 or x_position >= self.size or y_position < 0 or y_position >= self.size:
            print("You hit a wall!")
            return

        # Determine collisions
        cell = self.grid[y_position][x_position]
        if cell is None:
            output = "You move into the empty space."
        elif isinstance(cell, Obstacle):
            damage = cell.damage
            output = f"You hit a {cell.name} and take {damage} damage!"
            self.player.current_health -= damage
            if self.player.current_health <= 0:
                print("You have died.")
                sys.exit()
        elif isinstance(cell, Enemy):
            enemy_defeated = self.player.attack(cell)
            output = \
                self.player.message
            if enemy_defeated:
                self.grid[y_position][x_position] = None
        elif isinstance(cell, Exit):
            print(cell.message)
            sys.exit()

        self.grid[self.player_position[1]][self.player_position[0]] = None
        self.player_position = (x_position, y_position)
        self.grid[y_position][x_position] = self.player

        self.print_map()

        print(output)
