import random
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
            self.dice_vars.append(StringVar(value=roll_service.roll.dices[i]))
            self.d.append(ttk.Checkbutton(master=self._frame, textvariable=self.dice_vars[i]))
            self.d[i].grid(row=2, column=i+1)

        button = ttk.Button(
            master=self._frame,
            text="Roll dices",
            command=self._roll_dices
        )
        button.grid(row=3, column=0)

    def _roll_dices(self):
        if not game_service.turns_left():
            self._handle_end()
        game_service.play_turn()
        
        for i in range(5):
            if len(self.d[i].state()) == 0:
                self.dice_vars[i].set(str(random.randint(1,6)))
            else:
                self.dice_vars[i].set(self.dice_vars[i].get())

        self.scoreboard_var.set(game_service.game.scoreboard)
