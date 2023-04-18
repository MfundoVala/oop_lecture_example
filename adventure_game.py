"""
TODO: DOCSTRING
"""
import random
from player import Wizard,Warrior
from enemy import Goblin,Orc
from obstacles import Trap,Wall
from world import World, Exit



# Create a MySQL database connection here

def main():
    """
    TODO: DOCSTRING
    """

    world = None
    restore = input("Do you want to restore your previous game? (y/n): ")
    world = World(10)
    if restore.lower() == "y":
        player = random.choice([Warrior("asdasd"), Wizard("asdasd")])
        world.player = player
        world.get_stored_world()
        # Restore the player's data from the database
    else:
        player_type = input('''Choose your player type: 
        1. Warrior
        2. Wizard
        >>> ''')
        player_name = input("What is your name?: ")

        if player_type.lower() == "1":
            player = Warrior(player_name)
        elif player_type.lower() == "2":
            player = Wizard(player_name)
        else:
            print("Invalid player type.")

        def random_position():
            return random.randint(1, 9)

        world = World(10)
        world.player = player
        world.grid[0][0] = player
        world.grid[random_position()][random_position()] = Wall()
        world.grid[random_position()][random_position()] = Trap()
        world.grid[random_position()][random_position()] = Goblin()
        world.grid[random_position()][random_position()] = Orc()
        world.grid[random_position()][random_position()] = Exit("Congratulations! You have found"
                                                                 " the exit and beaten the game!")

    world.print_map()

    while True:
        direction = input('''Which direction do you want to move? 
        W - up
        S - down
        A - left
        D - right
        >>> ''').lower()
        world.move_player(direction)


if __name__ == "__main__":
    main()
