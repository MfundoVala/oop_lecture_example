"""
Main program
"""
import sqlite3
import database_manager
from world import World


def main():
    """
    Main loop creating or restoring player data then calls to World object
    to start game.
    """
    game_database = database_manager.DatabaseManager(sqlite3.connect("game_data.db"))
    restore = input("Do you want to restore your previous game? (y/n): ")
    current_world = World(10, game_database)

    if restore.lower() == "y":
        current_world.restore_previous_player()
        current_world.get_stored_world()
    else:
        name = input("What is your name?: ")
        current_world.create_new_player(name)
        current_world.populate_grid(5, 5)

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
