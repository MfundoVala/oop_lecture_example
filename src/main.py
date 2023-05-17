"""
Main program
"""
import sqlite3
from database_manager import DatabaseManager
from world import World


def main():
    """
    Main loop creating or restoring player data then calls to World object
    to start game.
    """
    game_database = DatabaseManager(sqlite3.connect("game_data.db"))
    current_world = World(10, game_database)

    while True:
        menu = input("***********GAME NAME***********\n"
                    "1. New Game\n"
                    "2. Restore previous game\n>")
        
        if menu == "1":
            name = input("What is your name?: ")
            current_world.create_new_player(name)
            current_world.populate_grid(5, 5)
            break
        if menu == "2":
            current_world.restore_previous_player()
            current_world.get_stored_world()
            break
        print("Unfortunately you have not selected one of the options.")

    while True:
        current_world.print_map()
        direction = input("Which direction do you want to move?\n"
                          "W - up\n"
                          "S - down\n"
                          "A - left\n"
                          "D - right\n"
                          ">>> ").lower()
        current_world.move_player(direction)


main()
