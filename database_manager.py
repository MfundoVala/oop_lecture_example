"""
Database manager module containing the DatabaseManager class definition.
"""

class DatabaseManager:
    """
    Creates a DatabaseManager object that is responsible for storing and
    retrieving data from database.
    """

    def __init__(self, database):
        self.database = database
        self.cursor = self.database.cursor()

    def save_player_data(self, player, position):
        """
        Saves player data to Player table in the database for world
        restoration later.
        """
        self.clear_db()
        self.cursor.execute("INSERT INTO Players(Type, Position, "
                            "Name, MaxHealth, CurrentHealth, Damage)"
                            "VALUES (?, ?, ?, ?, ?, ?)", (player.type, str(position), player.name,
                                                          player.max_health, player.current_health,
                                                          player.damage))
        self.database.commit()

    def save_obstacle(self, obstacle_type, position):
        """
        Stores obstacle data to the Obstacles table database for world
        restoration later.
        """
        self.clear_db()
        self.cursor.execute("INSERT INTO Players(?, ?)", (obstacle_type, position))
        self.database.commit()

    def clear_db(self):
        """
        Clears all previous entries in database tables.
        """
        self.cursor.execute("DELETE FROM Players")
        self.cursor.execute("DELETE FROM Obstacles")
        self.database.commit()

    def retrieve_player_data(self):
        """
        Retrieve player data from Player table in the database for world
        restoration.

        :return: data: Player data required for world restoration.
        """
        self.cursor.execute("SELECT * FROM Players")
        data = self.cursor.fetchone()
        return data
