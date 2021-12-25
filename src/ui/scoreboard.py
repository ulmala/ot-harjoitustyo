from tkinter import ttk
from services.game_service import game_service


class Scoreboard:
    """Class representing the visual scoreboard in the game.

    Attributes:
        scoreboard: game scoreboard to display
    """
    def __init__(self, frame, row, column, columnspan):
        """Class constructor

        Args:
            frame (ttk.Frame): root window
            row (int): row number where to grid widget
            column (int): col number where to grid widget
            columnspan (int): columnspan for the widget
        """
        self._frame = frame
        self._scoreboard = None
        self._row = row
        self._column = column
        self._columnspan = columnspan

    def initialize(self):
        """Initilaizes the scoreboard. Can be used also to display the updated scoreboard. Will always
        use the updated scoreboard data.
        """
        columns = game_service.get_player_names()
        columns.insert(0, 'turn')
        self._scoreboard = ttk.Treeview(master=self._frame,
                                       height=len(game_service.game.scoreboard.index),
                                       columns=columns)
        self._scoreboard.column('#0', width=0)
        for col in self._scoreboard['columns']:
            self._scoreboard.column(col, anchor='center', width=100)
            self._scoreboard.heading(col, text=col, anchor='center')

        for idx, row in game_service.game.scoreboard.iterrows():
            values = list(row.values)
            values.insert(0, idx)
            tags = []
            if idx == game_service.get_current_turn_name():
                tags = ['active_row']
            self._scoreboard.insert(parent='',
                                   index='end',
                                   iid=game_service.game.scoreboard.index.get_loc(idx),
                                   values=values,
                                   tags=tags)
        self._scoreboard.tag_configure('active_row', background='orange')
        self._scoreboard.grid(row=self._row, column=self._column, columnspan=self._columnspan)
