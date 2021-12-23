from tkinter import Toplevel, ttk, constants

from entities.player import Player
from entities.game import Game
from services.game_service import game_service

class StartView:
    def __init__(self, root, handle_game):
        self._root = root
        self._handle_game = handle_game
        self._frame = None
        self._top_scores = None
        self._player_entires = []

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _start_game_handler(self):
        for entry in self._player_entires:
            if len(entry.get()) > 0:
                game_service.add_player(entry.get())
        self._handle_game()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header_label = ttk.Label(master=self._frame, text='Yahtzee')
        header_label.grid(row=0, column=0)

        self._initialize_player_entries()
        start_button = ttk.Button(
            master=self._frame,text='Start',
            command=self._start_game_handler
        )

        start_button.grid(row=self._player_entires[-1].grid_info()['row'] + 1 , column=0)

        label = ttk.Label(self._frame, text='\n\nAll time top 5 scores')
        label.grid(row=self._player_entires[-1].grid_info()['row'] + 2, column=0)

        self._initialize_top_scoreboard()

    def _initialize_player_entries(self):
        for i in range(game_service.game.max_players):
            player_label = ttk.Label(master=self._frame, text=f'Player {i+1}')
            self._player_entires.append(ttk.Entry(master=self._frame))
            player_label.grid(row=(i+1) * 2 - 1, column=0)
            self._player_entires[-1].grid(row=(i+1)*2, column=0)

    def _initialize_top_scoreboard(self):
        self._top_scores = ttk.Treeview(master=self._frame,
                                        height=5,
                                        columns=['Player', 'Points'])
        self._top_scores.column('#0', width=0)
        for col in self._top_scores['columns']:
            self._top_scores.column(col, anchor='center', width=70)
            self._top_scores.heading(col, text=col, anchor='center')
        top_scores = game_service._game_repository.get_top_5_high_scores()
        for (i, row) in zip(range(5), top_scores):
            self._top_scores.insert(parent='',
                                    index='end',
                                    iid=i,
                                    values=(row[0], row[1]))
        self._top_scores.grid(row=self._player_entires[-1].grid_info()['row'] + 3, column=0)