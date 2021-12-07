from tkinter import ttk, constants
from services.game_service import game_service

class EndView:
    def __init__(self, root, handle_start):
        self._root = root
        self.handle_start = handle_start
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = self._root
        header_label = ttk.Label(master=self._frame, text='game ended')
        new_game_button = ttk.Button(master=self._frame, text='new game', command=self.handle_start)
        winner, points = game_service.declare_winner()
        winner_label = ttk.Label(master=self._frame,
                                 text=f'Winner is {winner}, with {points} points!')
        header_label.grid(row=0, column=0, columnspan=2)
        winner_label.grid(row=1, column=0)
        new_game_button.grid(row=2, column=0)