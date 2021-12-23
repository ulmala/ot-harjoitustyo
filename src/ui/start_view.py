from tkinter import ttk, constants

from entities.player import Player
from services.game_service import game_service

class StartView:
    def __init__(self, root, handle_game):
        self._root = root
        self._handle_game = handle_game
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _start_game_handler(self):
        if len(self._player1_entry.get()) > 0:
            player1_name = self._player1_entry.get()
            game_service.add_player(player1_name)
        if len(self._player2_entry.get()) > 0:
            player2_name = self._player2_entry.get()
            game_service.add_player(player2_name)
        self._handle_game()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header_label = ttk.Label(master=self._frame, text='Yahtzee')
        player1_label = ttk.Label(master=self._frame, text='Player 1')
        self._player1_entry = ttk.Entry(master=self._frame)
        player2_label = ttk.Label(master=self._frame, text='Player 1')
        self._player2_entry = ttk.Entry(master=self._frame)

        start_button = ttk.Button(
            master=self._frame,text='Start',
            command=self._start_game_handler
        )

        header_label.grid(row=0, column=1, columnspan=2)
        player1_label.grid(row=1, column=1)
        self._player1_entry.grid(row=2, column=1)
        player2_label.grid(row=1, column=2)
        self._player2_entry.grid(row=2, column=2)
        start_button.grid(row=3, column=1, columnspan=2)
