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
                print('\n\n')
                print('Pelaaja: ', player)
                points = roll_service.execute_roll(idx)
                game.scoreboard.at[idx, player] = points
            self.print_status()

    def declare_winner(self):
        self.print_status()
        game.scoreboard = game.scoreboard.astype(int)
        winner = game.scoreboard.sum().idxmax()
        points = game.scoreboard.sum().max()
        return winner,points
        
    def print_status(self):
        print('\n' * 50)
        print('################# TILANNE #################')
        print(game.scoreboard)

game_service = GameService()
