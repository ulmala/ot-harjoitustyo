from tkinter import ttk
from services.game_service import game_service


class Scoreboard:
    def __init__(self, frame, row, column, columnspan):
        self._frame = frame
        self.scoreboard = None
        self.row = row
        self.column = column
        self.columnspan = columnspan

    def initialize(self):
        columns = game_service.get_player_names()
        columns.insert(0, 'turn')
        self.scoreboard = ttk.Treeview(master=self._frame,
                                       height=len(game_service.game.scoreboard.index),
                                       columns=columns)
        self.scoreboard.column('#0', width=0)
        for col in self.scoreboard['columns']:
            self.scoreboard.column(col, anchor='center', width=100)
            self.scoreboard.heading(col, text=col, anchor='center')

        for idx, row in game_service.game.scoreboard.iterrows():
            values = list(row.values)
            values.insert(0, idx)
            tags = []
            if idx == game_service.get_current_turn_name():
                tags = ['active_row']
            self.scoreboard.insert(parent='',
                                   index='end',
                                   iid=game_service.game.scoreboard.index.get_loc(idx),
                                   values=values,
                                   tags=tags)
        self.scoreboard.tag_configure('active_row', background='orange')
        self.scoreboard.grid(row=self.row, column=self.column, columnspan=self.columnspan)
