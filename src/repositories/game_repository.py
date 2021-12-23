from db_connection import get_db_connection
class GameRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all_games(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from games")
        rows = cursor.fetchall()

        return [(row['winner'], row['points']) for row in rows]

    def insert_game(self, winner, points):
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into games (winner, points) values (?, ?)',
            (winner, points)
        )

        self._connection.commit()

        return True

game_repository = GameRepository(get_db_connection())