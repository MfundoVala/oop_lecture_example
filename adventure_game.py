"""
Main program
"""
import sqlite3
import database_manager
from player import Player
from world import World


def new_player(player_name):
    while True:
            player_type = input("Choose your player type:\n"
                                "1. Warrior\n"
                                "2. Wizard\n"
                                ">>> ")

            if player_type.lower() == "1":
                player = Player(player_name, 100, 10, "Warrior")
                break
            if player_type.lower() == "2":
                player = Player(player_name, 50, 20, "Wizard")
                break
            print("Invalid player type.")
    return player


def restore_previous_player(database):
    data = database.retrieve_player_data()
    if data[0] == "Warrior":
        player = Player(data[2], 100, 10, "Warrior")
    else:
        player = Player(data[2], 50, 20, "Wizard")
    player.current_health = data[4]

    return player


def main():
    """
    Main loop creating or restoring player data then calls to World object
    to start game.
    """
    game_database = database_manager.DatabaseManager(sqlite3.connect("game_data.db"))
    restore = input("Do you want to restore your previous game? (y/n): ")
    current_world = World(10, game_database)
    # Restore the player's data from the database or create new game.
    if restore.lower() == "y":
        player = restore_previous_player(game_database)
        current_world.player = player
        current_world.get_stored_world()
    else:
        name = input("What is your name?: ")
        player = new_player(name)
        current_world.player = player
        current_world.populate_grid(5)

    
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
