"""
TODO: DOCSTRING
"""

import sqlite3

class DatabaseManager:
    """
    TODO: DOCSTRING
    """

    def __init__(self):
        self.db = sqlite3.connect("game_data.db")
        self.cursor = self.db.cursor()

#        ARMAND TO FIX TO MANY ARGUMENTS ERRROR IN PYLINT PUT PLAYER OBJECT AS ARGUMENT
#        AND PLAYER POSITION AS 2ND ARGUMENT
    def save_player_data(self, player_type, position, name, max_health, current_health, damage):
        """
        TODO: DOCSTRING
        """
        self.clear_db()
        self.cursor.execute("INSERT INTO Players(Type, Position, "
                            "Name, MaxHealth, CurrentHealth, Damage)"
                            "VALUES (?, ?, ?, ?, ?, ?)", (player_type, str(position), name,
                            max_health, current_health, damage))
        self.db.commit()

    def save_obstacle(self, obstacle_type, position):
        """
        TODO: DOCSTRING
        """
        self.cursor.execute("INSERT INTO Players(?, ?)", (obstacle_type, position))
        self.db.commit()

    def clear_db(self):
        """
        TODO: DOCSTRING
        """
        self.cursor.execute("DELETE FROM Players")
        self.cursor.execute("DELETE FROM Obstacles")
        self.db.commit()

    def retrieve_player_data(self):
        """
        TODO: DOCSTRING
        """
        self.cursor.execute("SELECT * FROM Players")
        data = self.cursor.fetchall()
        return data
    