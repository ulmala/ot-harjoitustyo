from entities.game import game
from services.roll_service import roll_service

class GameService:

    def add_player(self, player):
        if len(game.players) < game.max_players:
            game.players.append(player)
            game.scoreboard[player.name] = '-'
            return True
        return False

    def start_game(self):
        for idx in game.scoreboard.index:
            for player in game.scoreboard.columns:
                points = roll_service.execute_roll(idx)
                game.scoreboard.at[idx, player] = points
                self.print_status()
        self.declare_winner()

    def declare_winner(self):
        game.scoreboard = game.scoreboard.astype(int)
        winner = game.scoreboard.sum().idxmax()
        points = game.scoreboard.sum().max()
        print(f'WINNER IS {winner} with {points} points!')

    def print_status(self):
        print()
        print('##### CURRENT_STATUS #####')
        print(game.scoreboard)
        print()

game_service = GameService()
