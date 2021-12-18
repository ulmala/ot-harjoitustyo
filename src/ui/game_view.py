from tkinter import ttk, constants, StringVar
from services.game_service import game_service
from services.roll_service import roll_service

class GameView:
    def __init__(self, root, handle_end):
        self._root = root
        self._handle_end = handle_end
        self._frame = None

        self.scoreboard_var = None
        self.dice_vars = []
        self.d = []
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.scoreboard_var = StringVar(value=game_service.game.scoreboard)
        scoreboard = ttk.Label(master=self._frame, textvariable=self.scoreboard_var)
        scoreboard.grid(row=0, column=0)

        for i in range(5):
            self.dice_vars.append(
                StringVar(
                    value=game_service.dices[i]
                    )
                )
            self.d.append(
                ttk.Checkbutton(
                    master=self._frame,
                    textvariable=self.dice_vars[i]
                    )
                )
            self.d[i].grid(row=2, column=i+1)

        self.roll_button = ttk.Button(
            master=self._frame,
            text="Roll dices",
            command=self._roll_dices
        )
        self.roll_button.grid(row=3, column=0)

        self.debug_var = StringVar(value=game_service.dices)
        debug_label = ttk.Label(master=self._frame, textvariable=self.debug_var)
        debug_label.grid(row=4, column=0)

        self.debug_var2 = StringVar(value=[len(d.state()) for d in self.d])
        debug_label2 = ttk.Label(master=self._frame, textvariable=self.debug_var2)
        debug_label2.grid(row=5, column=0)

        self.current_turn_var = StringVar(value=game_service.get_current_turn_name())
        current_turn_label = ttk.Label(master=self._frame, textvariable=self.current_turn_var)
        current_turn_label.grid(row=6, column=0)

        self.current_player_var = StringVar(value=game_service.get_current_player())
        current_player_label = ttk.Label(master=self._frame, textvariable=self.current_player_var)
        current_player_label.grid(row=7, column=0)

        self.throws_left_var = StringVar(value=f'{game_service.throws}/3')
        throws_left_label = ttk.Label(master=self._frame, textvariable=self.throws_left_var)
        throws_left_label.grid(row=8, column=0)

    def _roll_dices(self):    
        rolled_dices = game_service.roll_dices([len(d.state()) for d in self.d])
        
        game_service.throws -= 1 # pois käly logiikasta

        self.debug_var.set(rolled_dices)
        self.debug_var2.set([len(d.state()) for d in self.d])

        for i in range(5):
            self.dice_vars[i].set(game_service.dices[i])


        self.current_player_var.set(game_service.get_current_player())
        self.current_turn_var.set(game_service.get_current_turn_name())
        self.throws_left_var.set(f'{game_service.throws}/3')
        self.scoreboard_var.set(game_service.game.scoreboard)
    


    def _hide_roll_button(self):
        print('lol')
        self.roll_button.grid_forget()
        self.start_turn_button = ttk.Button(
            master=self._frame,
            text="Next turn",
            #command=self._roll_dices
        )
        self.start_turn_button.grid(row=3, column=0)
