from tkinter import ttk, constants, StringVar
from services.game_service import game_service

class GameView:
    def __init__(self, root, handle_end):
        self._root = root
        self._handle_end = handle_end
        self._frame = None

        self.dice_vars = []
        self.dice_checkbuttons = []
        self.scoreboard = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_scoreboard(self):
        columns = game_service.get_player_names()
        columns.insert(0, 'turn')
        self.scoreboard = ttk.Treeview(master=self._frame,
                                      height=len(game_service.game.scoreboard.index),
                                      columns=columns)
        self.scoreboard.column('#0', width=0)
        for col in self.scoreboard['columns']:
            self.scoreboard.column(col, anchor='center', width=80)
            self.scoreboard.heading(col, text=col,anchor='center')

        for idx, row in game_service.game.scoreboard.iterrows():
            values = list(row.values)
            values.insert(0, idx)
            self.scoreboard.insert(parent='',
                                  index='end',
                                  iid=game_service.game.scoreboard.index.get_loc(idx),
                                  values=values)
        self.scoreboard.grid(row=0, column=0, columnspan=5)


    def _initialize_dices(self):
        for i in range(5):
            self.dice_vars.append(StringVar(value=game_service.dices[i]))
            self.dice_checkbuttons.append(
                ttk.Checkbutton(
                    master=self._frame,
                    textvariable=self.dice_vars[i]
                    )
                )
            self.dice_checkbuttons[i].grid(row=2, column=i)
        self._deselect_dices()

    def _initialize_game_status_labels(self):
        self.current_turn_var = StringVar(value=game_service.get_current_turn_name())
        current_turn_label = ttk.Label(master=self._frame, textvariable=self.current_turn_var)
        current_turn_label.grid(row=6, column=0)

        self.current_player_var = StringVar(value=game_service.get_current_player())
        current_player_label = ttk.Label(master=self._frame, textvariable=self.current_player_var)
        current_player_label.grid(row=7, column=0)

        self.throws_left_var = StringVar(value=f'{game_service.throws}/3')
        throws_left_label = ttk.Label(master=self._frame, textvariable=self.throws_left_var)
        throws_left_label.grid(row=8, column=0)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_game_status_labels()
        self._initialize_dices()
        self._initialize_scoreboard()
        
        self.roll_dices_button = ttk.Button(
            master=self._frame,
            text="Roll dices",
            command=self._roll_dices
        )
        self.roll_dices_button.grid(row=3, column=0)

    def _roll_dices(self):    
        game_service.roll_dices([len(dice.state()) for dice in self.dice_checkbuttons])
        game_service.throws -= 1

        for i in range(5):
            self.dice_vars[i].set(game_service.dices[i])

        self._update_game_status_labels()

        if game_service.throws == 0 or self._player_keeps_all_dices():
            self._hide_roll_button()
        
    def _hide_roll_button(self):
        self.roll_dices_button = ttk.Button(
            master=self._frame,
            text="Next turn",
            command=self._proceed_to_next_turn
        )
        self.roll_dices_button.grid(row=3, column=0)

    def _proceed_to_next_turn(self):
        game_service.next_turn()
        self.roll_dices_button.grid_forget()
        self._update_game_status_labels()
        self._deselect_dices()

    def _update_game_status_labels(self):
        self.current_player_var.set(game_service.get_current_player())
        self.current_turn_var.set(game_service.get_current_turn_name())
        self.throws_left_var.set(f'{game_service.throws}/3')
        self._initialize_scoreboard()


    def _deselect_dices(self):
        """Loops through all dice checkbuttons and invokes the checkbutton 
        until it's state is unchecked.
        """
        for i in range(5):
            while len(self.dice_checkbuttons[i].state()) != 0:
                self.dice_checkbuttons[i].invoke()

    def _player_keeps_all_dices(self):
        """Checks if player has checked all dice checkbuttons (wants to keep all dices)

        Returns:
            bool: True if all checkbuttons are checked, else False
        """
        if all(dice == 1 for dice in [len(dice.state()) for dice in self.dice_checkbuttons]):
            return True
        return False