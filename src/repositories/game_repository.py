from db_connection import get_db_connection


class GameRepository:
    """Class responsible for all datbase operations.
    Attributes:
        connection: connection for the database
    """
    def __init__(self, connection):
        """Class constructor

        Args:
            connection (sqlite3.connection): connection to the sqlite3 database
        """
        self._connection = connection

    def get_top_5_high_scores(self):
        """Fetches top 5 highscores (player and points) from the database

        Returns:
            list: list of tuples (player, points)
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'select winner, points from games order by points desc limit 5'
        )
        rows = cursor.fetchall()
        return [(row['winner'], row['points']) for row in rows]

    def insert_game(self, scoreboard, winner, points):
        """Inserts game scoreboard, name of the winner, winner's points into the database.

        Args:
            scoreboard (pd.DataFrame): scoreboard as pandas dataframe
            winner (str): name of the winner player
            points (int): points of the winner

        Returns:
            bool: True if database operation succeeded
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into games (scoreboard, winner, points) values (?, ?, ?)',
            (scoreboard, winner, points)
        )
        self._connection.commit()
        return True


game_repository = GameRepository(get_db_connection())
