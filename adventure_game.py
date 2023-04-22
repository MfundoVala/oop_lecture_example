"""
Main program
"""
import random
import sqlite3
import database_manager
from player import Player
from obstacles import Obstacle
from enemy import Enemy
from world import World, Exit


def random_position():
    """:return: Random number between 1 and 9"""
    return random.randint(1, 9)


def main():
    """
    Main loop creating or restoring player data then calls to World object
    to start game.
    """
    game_database = database_manager.DatabaseManager(sqlite3.connect("game_data.db"))

    restore = input("Do you want to restore your previous game? (y/n): ")
    player_name = input("What is your name?: ")
    current_world = World(10, game_database)
    # Restore the player's data from the database or create new game.
    if restore.lower() == "y":
        player = random.choice([Player(player_name, 100, 10, "Warrior"),
                                Player(player_name, 20, 20, "Wizard")])

        current_world.player = player
        current_world.get_stored_world()
    else:
        while True:
            player_type = input("Choose your player type:\n"
                                "1. Warrior\n"
                                "2. Wizard\n"
                                ">>> ")


            if player_type.lower() == "1":
                player = Player(player_name, 100, 10, "Warrior")
                break
            if player_type.lower() == "2":
                player = Player(player_name, 20, 20, "Wizard")
                break
            print("Invalid player type.")

        current_world.player = player
        current_world.populate_grid()

    current_world.print_map()

    while True:
        direction = input("Which direction do you want to move?\n"
                          "W - up\n"
                          "S - down\n"
                          "A - left\n"
                          "D - right\n"
                          ">>> ").lower()
        current_world.move_player(direction)


main()
