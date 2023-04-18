import sqlite3

class DatabaseManager:

    def __init__(self):
        self.db = sqlite3.connect("game_data.db")
        self.cursor = self.db.cursor()

    def save_player_data(self, player_type, position, name, max_health, current_health, damage):
        self.clear_db()
        self.cursor.execute("INSERT INTO Players(Type, Position, Name, MaxHealth, CurrentHealth, Damage)"
                            "VALUES (?, ?, ?, ?, ?, ?)", (player_type, str(position), name,
                            max_health, current_health, damage))
        self.db.commit()

    def save_obstacle(self, obstacle_type, position):
        self.cursor.execute("INSERT INTO Players(?, ?)", (obstacle_type, position))
        self.db.commit()

    def clear_db(self):
        self.cursor.execute("DELETE FROM Players")
        self.cursor.execute("DELETE FROM Obstacles")
        self.db.commit()

    def retrieve_player_data(self):
        self.cursor.execute("SELECT * FROM Players")
        data = self.cursor.fetchall()
        return data