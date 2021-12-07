from ui.start_view import StartView
from ui.game_view import GameView
from ui.end_view import EndView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_start(self):
        self._show_start_view()

    def _handle_game(self):
        self._show_game_view()

    def _handle_end(self):
        self._show_end_view()

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._handle_game
        )

        self._current_view.pack()

    def _show_game_view(self):
        self._hide_current_view()

        self._current_view = GameView(
            self._root,
            self._handle_end
        )

        self._current_view.pack()

    def _show_end_view(self):
        self._hide_current_view()

        self._current_view = EndView(
            self._root,
            self._handle_start
        )

        self._current_view.pack()