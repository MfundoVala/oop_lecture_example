"""
This module contains the World class, which is used 
to create a world for the player to explore.
"""
import random
import sys
import os
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

    def __init__(self, size, database):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size) ]
        self.player_position = (0, 0)
        self.database = database
        self.player = None
        self.message = ""

    def create_new_player(self, player_name):
        """Create new player."""
        while True:
            player_type = input("Choose your player type:\n"
                                "1. Warrior\n"
                                "2. Wizard\n"
                                ">>> ")

            if player_type.lower() == "1":
                self.player = Player(player_name, 100, 10, "Warrior")
                break
            if player_type.lower() == "2":
                self.player = Player(player_name, 50, 20, "Wizard")
                break
            print("Invalid player type.")

    def restore_previous_player(self):
        """Restores player data from previous game"""
        data = self.database.retrieve_player_data()
        if data[0] == "Warrior":
            self.player = Player(data[2], 100, 10, "Warrior")
        else:
            self.player = Player(data[2], 50, 20, "Wizard")
        self.player.current_health = data[4]

    def print_map(self):
        """
        Print world map to terminal.
        """
        os.system('cls')
        for row in self.grid:
            for cell in row:
                if cell is None:
                    print(".", end="")
                elif isinstance(cell, Player):
                    print("P", end="")
                elif isinstance(cell, Obstacle):
                    print(cell.prefix, end="")
                elif isinstance(cell, Enemy):
                    print(cell.prefix, end="")
                elif isinstance(cell, Exit):
                    print("X", end="")
            print()
        print(self.message)
        print(f"Current health:  {self.player.current_health}")
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
                        self.grid[x_position][y_position] = self.player
                        self.player_position = (x_position, y_position)

    def move_player(self, direction):
        """
        Move player to given direction and detect if a collision has occurred.
        :param direction: Direction player moves in.
        """

        x_position, y_position = self.player_position
        if direction in ("w", "up"):
            x_position -= 1
        elif direction in ("s", "down"):
            x_position += 1
        elif direction in ("a", "left"):
            y_position -= 1
        elif direction in ("d", "right"):
            y_position += 1

        if not self.determine_wall_collision(x_position, y_position):

            self.determine_collision(x_position, y_position)

            self.grid[self.player_position[0]][self.player_position[1]] = None
            self.player_position = (x_position, y_position)
            self.grid[x_position][y_position] = self.player


    def determine_wall_collision(self, x_pos, y_pos):
        """
        Determine if player is colliding with a wall.

        :param: x_pos: x position of new cell.
        :param: y_pos: y position of new cell.
        """
        if x_pos < 0 or x_pos >= self.size or y_pos < 0 or y_pos >= self.size:
            self.print_map()
            return True
        return False


    def determine_collision(self, new_x, new_y):
        """
        Determine object in cell player is moving to and calls to appropriate functions.

        :param: new_x: x position of new cell.
        :param: new_x: y position of new cell.
        """
        cell = self.grid[new_x][new_y]
        if cell is None:
            self.message = "You move into the empty space."
        elif isinstance(cell, Obstacle):
            self.message = f"You hit a {cell.name} and take {cell.damage} damage!"
            self.player.take_damage(cell.damage)
            if self.player.is_dead():
                print("You have died.")
                sys.exit()
        elif isinstance(cell, Enemy):
            enemy_defeated = self.player.attack(cell)
            self.message = self.player.message
            if enemy_defeated:
                self.grid[new_x][new_y] = None
        elif isinstance(cell, Exit):
            print(cell.message)
            sys.exit()

    def populate_grid(self, total_enemies = 2, total_obstacles = 3):
        """
        Populates the world object's grid with the player, enemies and obstacles.

        :param: total_enemies: Amount of enemies to add.
        :param: total_obstacles: Amount of obstacles to add.
        """
        self.grid[0][0] = self.player

        for i in range(total_enemies):
            while True:
                temp_x, temp_y = (random.randrange(0, 9), random.randrange(0, 9))
                if self.grid[temp_x][temp_y] is None:
                    enemy_type = random.choice([Enemy("Goblin", 20, 50), Enemy("Orc", 30, 10)])
                    self.grid[temp_x][temp_y] = enemy_type
                    break
        for i in range(total_obstacles):
            while True:
                temp_x, temp_y = (random.randrange(0, 9), random.randrange(0, 9))
                if self.grid[temp_x][temp_y] is None:
                    obstacle_type = random.choice([Obstacle("Wall", 10), Obstacle("Trap", 20)])
                    self.grid[temp_x][temp_y] = obstacle_type
                    break
        while True:
            temp_x, temp_y = (random.randrange(0, 9), random.randrange(0, 9))
            if self.grid[temp_x][temp_y] is None:
                temp_x, temp_y = (random.randrange(0, 9), random.randrange(0, 9))
                self.grid[temp_x][temp_y] = Exit("Congratulations! You have"
                                       " found the exit and "
                                       "beaten the game!")
                break
