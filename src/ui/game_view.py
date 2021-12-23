from tkinter import ttk, constants, StringVar, PhotoImage
from services.game_service import game_service


class GameView:
    def __init__(self, root, handle_end):
        self._root = root
        self._handle_end = handle_end
        self._frame = None

        self._dice_vars  = []
        self._dice_checkbuttons = []
        self._scoreboard = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize_scoreboard(self):
        columns = game_service.get_player_names()
        columns.insert(0, 'turn')
        self._scoreboard = ttk.Treeview(master=self._frame,
                                      height=len(game_service.game.scoreboard.index),
                                      columns=columns)
        self._scoreboard.column('#0', width=0)
        for col in self._scoreboard['columns']:
            self._scoreboard.column(col, anchor='center', width=40 + len(game_service.get_players())*15)
            self._scoreboard.heading(col, text=col,anchor='center')

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
        self._scoreboard.grid(row=0, column=0, columnspan=5)


    def _initialize_dices(self):
        for i in range(5):
            self._dice_vars .append(StringVar(value=game_service.get_dices()[i]))
            self._dice_checkbuttons.append(
                ttk.Checkbutton(
                    master=self._frame,
                    textvariable=self._dice_vars[i]
                    )
                )
            self._dice_checkbuttons[i].grid(row=2, column=i)
        self._deselect_dices()

    def _initialize_game_status_labels(self):
        self.current_turn_var = StringVar(value=game_service.get_current_turn_name())
        current_turn_label = ttk.Label(master=self._frame, textvariable=self.current_turn_var)
        current_turn_label.grid(row=6, column=0)

        self.current_player_var = StringVar(value=game_service.get_current_player())
        current_player_label = ttk.Label(master=self._frame, textvariable=self.current_player_var)
        current_player_label.grid(row=7, column=0)

        self.throws_left_var = StringVar(value=f'{game_service.get_throws_left()}/3')
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

        self.debug_var = StringVar(value=(game_service.get_current_turn(), game_service.get_current_turn_name()))
        debug_label = ttk.Label(master=self._frame, textvariable=self.debug_var)
        debug_label.grid(row=9, column=0)

    def _roll_dices(self):
        self._set_dice_checkbutton_state('normal')
        game_service.roll_dices([len(dice.state()) for dice in self._dice_checkbuttons])
        game_service.game.throws -= 1
        self._update_dice_vars()
        self._update_game_status_labels()

        if game_service.get_throws_left() == 0 or self._player_keeps_all_dices():
            game_service.update_points()
            self._hide_roll_button()

    def _update_dice_vars(self):
        for i in range(5):
            self._dice_vars[i].set(game_service.get_dices()[i])

    def _hide_roll_button(self):
        self.roll_dices_button = ttk.Button(
            master=self._frame,
            text="Next turn",
            command=self._proceed_to_next_turn
        )
        self.roll_dices_button.grid(row=3, column=0)

    def _proceed_to_next_turn(self):
        game_ends = game_service.new_turn()
        if not game_ends:
            self._handle_end()
        else:
            self.roll_dices_button.grid_forget()
            self._update_game_status_labels()
            self._deselect_dices()
            self._set_dice_checkbutton_state(constants.DISABLED)

    def _set_dice_checkbutton_state(self, state):
        for dice_checkbutton in self._dice_checkbuttons:
            dice_checkbutton.config(state=state)
    
    def _update_game_status_labels(self):
        self.current_player_var.set(game_service.get_current_player())
        self.current_turn_var.set(game_service.get_current_turn_name())
        self.throws_left_var.set(f'{game_service.get_throws_left()}/3')
        self.debug_var.set((game_service.get_current_turn(), game_service.get_current_turn_name()))
        self._initialize_scoreboard()


    def _deselect_dices(self):
        """Loops through all dice checkbuttons and invokes the checkbutton 
        until it's state is unchecked.
        """
        for i in range(5):
            while len(self._dice_checkbuttons[i].state()) != 0:
                self._dice_checkbuttons[i].invoke()

    def _player_keeps_all_dices(self):
        """Checks if player has checked all dice checkbuttons (wants to keep all dices)

        Returns:
            bool: True if all checkbuttons are checked, else False
        """
        if all(dice == 1 for dice in [len(dice.state()) for dice in self._dice_checkbuttons]):
            return True
        return False