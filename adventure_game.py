import random

# Create a MySQL database connection here


class Player:
    
    def __init__(self, name, max_hp, damage, gold):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.damage = damage
        self.gold = gold
        self.message = ""
        self.save()

    def attack(self, enemy):
        damage = random.randint(1, self.damage)
        enemy.current_hp -= damage
        self.message = f"{self.name} deals {damage} damage to {enemy.name}!"
        if enemy.current_hp <= 0:
            self.gold += enemy.gold
            self.message += "\n" + f"{self.name} has defeated {enemy.name} and gained {enemy.gold} gold!"
            return True
        return False

    def save(self):
        # Save the player's data to the database
        pass


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, 100, 10, 0)


class Wizard(Player):
    def __init__(self, name):
        super().__init__(name, 20, 20, 0)


class Obstacle:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.save()

    def save(self):
        # Save the obstacle's data to the database
        pass


class Wall(Obstacle):
    def __init__(self):
        super().__init__("Wall", 10)


class Trap(Obstacle):
    def __init__(self):
        super().__init__("Trap", 20)


class Health:
    def __init__(self, amount):
        self.amount = amount
        self.save()

    def save(self):
        # Save the health item's data to the database
        pass


class Armour:
    def __init__(self, amount):
        self.amount = amount
        self.save()

    def save(self):
        # Save the armour item's data to the database
        pass


class Enemy:
    def __init__(self, name, max_hp, damage, gold):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.damage = damage
        self.gold = gold
        self.message = ""
        self.save()

    def attack(self, player):
        damage = self.damage
        player.current_hp -= damage
        self.message = f"The {self.name} deals {damage} damage to {player.name}!"

    def save(self):
        # Save the enemy's data to the database
        pass


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 20, 50, 10)


class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 30, 10, 20)


class Exit:
    def __init__(self, message):
        self.message = message


class World:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.player_position = (0, 0)

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
            output = ("You move into the empty space.")
        elif isinstance(cell, Obstacle):
            damage = cell.damage
            output = (f"You hit a {cell.name} and take {damage} damage!")
            self.player.current_hp -= damage
            if self.player.current_hp <= 0:
                output = ("You have died.")
                exit()
        elif isinstance(cell, Enemy):
            enemy_defeated = self.player.attack(cell)
            output = (self.player.message)
            if enemy_defeated:
                self.grid[y][x] = None
        elif isinstance(cell, Health):
            self.player.current_hp += cell.amount
            output = (f"You found a health potion and healed for {cell.amount} HP!")
            self.grid[y][x] = None
        elif isinstance(cell, Armour):
            self.player.max_hp += cell.amount
            self.player.current_hp += cell.amount
            output = (f"You found a piece of armour and increased your maximum HP by {cell.amount}!")
            self.grid[y][x] = None
        elif isinstance(cell, Exit):
            output = (cell.message)
            exit()

        self.grid[self.player_position[1]][self.player_position[0]] = None
        self.player_position = (x, y)
        self.grid[y][x] = self.player
        self.print_map()
        print(output)


def main():
    world = None
    restore = input("Do you want to restore your previous game? (y/n): ")
    if restore.lower() == "y":
        # Restore the player's data from the database
        pass
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
            exit()

        world = World(10)
        world.player = player
        world.grid[0][0] = player
        world.grid[4][4] = Wall()
        world.grid[3][6] = Trap()
        world.grid[5][5] = Goblin()
        world.grid[7][7] = Orc()
        world.grid[8][8] = Health(20)
        world.grid[2][2] = Armour(10)
        world.grid[9][9] = Exit("Congratulations! You have found the exit and beaten the game!")

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
