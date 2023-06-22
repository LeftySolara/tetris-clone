import pygame
import enum
import tetris.event
from transitions import Machine


class States(enum.Enum):
    """An enum representing the various game states."""

    UNKNOWN = enum.auto()  # Unknown state, indicating error or misconfiguration
    INITIALIZING = enum.auto()  # Game is initializing.
    INITIALIZED = enum.auto()  # Game has finished initializing.
    GAME_PLAYING = enum.auto()  # Game is running normally.
    MAIN_MENU = enum.auto()  # Game is displaying the main menu.
    GAME_ENDED = enum.auto()  # Game is displaying the "game over" screen.
    QUITTING = enum.auto()  # Game is exiting.


class GameState(Machine):
    """An object representing the game's state.

    This object contains a finite state machine that houses states
    and transitions related to game state.
    """

    transitions = [
        ["initialize", States.UNKNOWN, States.INITIALIZING],
        ["finish_initializing", States.INITIALIZING, States.INITIALIZED],
        ["open_main_menu", States.INITIALIZED, States.MAIN_MENU],
        ["open_main_menu", States.GAME_ENDED, States.MAIN_MENU],
        ["start_game", States.MAIN_MENU, States.GAME_PLAYING],
        ["end_game", States.GAME_PLAYING, States.GAME_ENDED],
        ["quit", States.GAME_ENDED, States.QUITTING],
        ["finish_quitting", States.QUITTING, States.UNKNOWN],
    ]

    def __init__(self):
        Machine.__init__(
            self,
            model=self,
            states=States,
            transitions=GameState.transitions,
            initial=States.UNKNOWN,
            auto_transitions=False,
            before_state_change="assign_prev_state",
            after_state_change="post_state_change",
        )
        self.prev_state = States.UNKNOWN

    def assign_prev_state(self):
        self.prev_state = self.state

    def post_state_change(self):
        pygame.event.post(
            pygame.event.Event(
                tetris.event.GAME_STATE_CHANGE,
                {"prev": self.prev_state, "current": self.state},
            )
        )
