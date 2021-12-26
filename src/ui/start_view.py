import webbrowser
from tkinter import ttk
from services.game_service import game_service

class StartView:
    def __init__(self, root, handle_game):
        self._root = root
        self._handle_game = handle_game
        self._frame = None
        self._top_scores = None
        self._player_entries = []

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _start_game_handler(self):
        if all([len(entry.get()) == 0 for entry in self._player_entries]):
            return
        for entry in self._player_entries:
            if len(entry.get()) > 0:
                game_service.add_player(entry.get())
        self._handle_game()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header_label = ttk.Label(master=self._frame, text='Yahtzee', font=('TkDefaultFont', 30))
        header_label.grid(row=0, column=0, pady=(0,25))

        self._initialize_link_to_rules()

        self._initialize_player_entries()

        start_button = ttk.Button(
            master=self._frame,text='Start',
            command=self._start_game_handler
        )
        start_button.grid(row=self._player_entries[-1].grid_info()['row'] + 1 , column=0)

        self._initialize_top_scoreboard()

    def _initialize_link_to_rules(self):
        link_to_rules = ttk.Label(master=self._frame,
                                 text='Click here to open game rules',
                                 foreground='orange',
                                 cursor='hand2', 
                                 font=('TkDefaultFont 15 underline bold')
        )
        link_to_rules.grid(row=1, column=0, pady=(0,20))
        link_to_rules.bind("<Button-1>", lambda x: webbrowser.open_new('https://en.wikipedia.org/wiki/Yahtzee#Rules'))

    def _initialize_player_entries(self):
        for i in range(1, game_service.game.max_players + 1):
            player_label = ttk.Label(master=self._frame, text=f'Player {i}')
            self._player_entries.append(ttk.Entry(master=self._frame))
            player_label.grid(row=(i+1) * 2 - 1, column=0)
            self._player_entries[-1].grid(row=(i+1)*2, column=0)

    def _initialize_top_scoreboard(self):
        label = ttk.Label(self._frame, text='All time top 5 scores')
        label.grid(row=self._player_entries[-1].grid_info()['row'] + 2, column=0, pady=(25,0))
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
        self._top_scores.grid(row=self._player_entries[-1].grid_info()['row'] + 3, column=0)