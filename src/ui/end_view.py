from tkinter import ttk
from services.game_service import game_service
from entities.game import Game
from ui.scoreboard import Scoreboard

class EndView:
    def __init__(self, root, handle_start):
        self._root = root
        self._handle_start = handle_start
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        scoreboard = Scoreboard(self._frame, row=2, column=0, columnspan=1)
        scoreboard.initialize()

        header_label = ttk.Label(master=self._frame,
                                 text='Game ended',
                                 font=('TkDefaultFont', 30))
        header_label.grid(row=0, column=0, pady=(0,25))

        winner, points = game_service.declare_winner()
        winner_label = ttk.Label(master=self._frame,
                                 text=f'Winner is {winner}with {points} points!',
                                 font=('TkDefaultFont', 20))
        winner_label.grid(row=1, column=0, pady=(0,15))

        new_game_button = ttk.Button(master=self._frame, text='new game', command=self._new_game)
        new_game_button.grid(row=3, column=0)

    def _new_game(self):
        game_service.game = Game()
        self._handle_start()
