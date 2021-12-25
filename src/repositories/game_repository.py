import pandas as pd
from io import StringIO
from db_connection import get_db_connection


class GameRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all_games(self):
        cursor = self._connection.cursor()
        cursor.execute('select * from games')
        rows = cursor.fetchall()

        for row in rows:
            id = row['id']
            scoreboard = pd.read_csv(StringIO(row['scoreboard']), sep=';')
            winner = row['winner']
            points = row['points']
        return id, scoreboard, winner, points


    def get_top_5_high_scores(self):
        cursor = self._connection.cursor()
        cursor.execute(
            'select winner, points from games order by points desc limit 5'
        )
        rows = cursor.fetchall()
        return [(row['winner'], row['points']) for row in rows]

    def insert_game(self, scoreboard, winner, points):
        cursor = self._connection.cursor()
        cursor.execute(
            'insert into games (scoreboard, winner, points) values (?, ?, ?)',
            (scoreboard, winner, points)
        )
        self._connection.commit()
        return True


game_repository = GameRepository(get_db_connection())