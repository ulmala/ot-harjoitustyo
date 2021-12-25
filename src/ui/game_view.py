from tkinter import ttk, constants, StringVar
from services.game_service import game_service
from ui.scoreboard import Scoreboard


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
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize_dices(self):
        dices_header = ttk.Label(master=self._frame, text='Dices', font=('TkDefaultFont', 18))
        dices_header.grid(column=0, row=1, columnspan=5, pady=(10,10))
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
        self._current_player_var = StringVar(
            value=f'Player in turn: {game_service.get_current_player()}'
        )
        current_player_label = ttk.Label(master=self._frame, textvariable=self._current_player_var)
        current_player_label.grid(column=0, row=4, columnspan=5)

        self._throws_left_var = StringVar(
            value=f'Throws left: {game_service.get_throws_left()}/3'
        )
        throws_left_label = ttk.Label(master=self._frame, textvariable=self._throws_left_var)
        throws_left_label.grid(row=5, column=0, columnspan=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.scoreboard = Scoreboard(self._frame, row=0, column=0, columnspan=5)
        self.scoreboard.initialize()

        self._initialize_game_status_labels()
        self._initialize_dices()
        
        self.roll_dices_button = ttk.Button(
            master=self._frame,
            text="Roll dices",
            command=self._roll_dices
        )
        self.roll_dices_button.grid(row=3, column=0, columnspan=5, pady=(25,0))

    def _roll_dices(self):
        self._set_dice_checkbutton_state(constants.NORMAL)
        game_service.roll_dices([len(dice.state()) for dice in self._dice_checkbuttons])
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
        self.roll_dices_button.grid(row=3, column=0, columnspan=5, pady=(25,0))

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
        self._current_player_var.set(f'Player in turn: {game_service.get_current_player()}')
        self._throws_left_var.set(f'Throws left: {game_service.get_throws_left()}/3')
        self.scoreboard.initialize()

    def _deselect_dices(self):
        for i in range(5):
            while len(self._dice_checkbuttons[i].state()) != 0:
                self._dice_checkbuttons[i].invoke()

    def _player_keeps_all_dices(self):
        if all(dice == 1 for dice in [len(dice.state()) for dice in self._dice_checkbuttons]):
            return True
        return False