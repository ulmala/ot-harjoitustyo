import random
from tkinter import ttk, constants, StringVar
from services.game_service import game_service

class GameView:
    def __init__(self, root, handle_end):
        self._root = root
        self._handle_end = handle_end
        self._frame = None

        self.scoreboard_var = None

        self.d1 = None
        self.d2 = None
        self.d3 = None
        self.d4 = None
        self.d5 = None

        self._d1_var = None
        self._d2_var = None
        self._d3_var = None
        self._d4_var = None
        self._d5_var = None

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

        self._d1_var = StringVar(value=':(')
        self._d2_var = StringVar(value=':(')
        self._d3_var = StringVar(value=':(')
        self._d4_var = StringVar(value=':(')
        self._d5_var = StringVar(value=':(')

        dices = ttk.Label(master=self._frame, text=f"""Dices (NOTE! these dices are note connected to the game logic yet. One can test the functionality to [un]keep dices by [de]selecting these boxes):""")
        self.d1 = ttk.Checkbutton(master=self._frame, textvariable=self._d1_var)
        self.d2 = ttk.Checkbutton(master=self._frame, textvariable=self._d2_var)
        self.d3 = ttk.Checkbutton(master=self._frame, textvariable=self._d3_var)
        self.d4 = ttk.Checkbutton(master=self._frame, textvariable=self._d4_var)
        self.d5 = ttk.Checkbutton(master=self._frame, textvariable=self._d5_var)
        dices.grid(row=1, column=0)
        self.d1.grid(row=2, column=1)
        self.d2.grid(row=2, column=2)
        self.d3.grid(row=2, column=3)
        self.d4.grid(row=2, column=4)
        self.d5.grid(row=2, column=5)

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

        self._d1_var.set(str(
                random.randint(1,6) if len(self.d1.state()) == 0 else self._d1_var.get()
            )
        )
        self._d2_var.set(str(
                random.randint(1,6) if len(self.d2.state()) == 0 else self._d2_var.get()
            )
        )
        self._d3_var.set(str(
                random.randint(1,6) if len(self.d3.state()) == 0 else self._d3_var.get()
            )
        )
        self._d4_var.set(str(
                random.randint(1,6) if len(self.d4.state()) == 0 else self._d4_var.get()
            )
        )
        self._d5_var.set(str(
                random.randint(1,6) if len(self.d5.state()) == 0 else self._d5_var.get()
            )
        )
        self.scoreboard_var.set(game_service.game.scoreboard)