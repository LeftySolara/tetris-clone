import pygame
import tetris.event.game_event as game_event
from transitions import Machine


class GameState(Machine):
    """An object representing the game's state.

    This object contains a finite state machine that houses states
    and transitions related to game state.
    """

    states = [
        "unknown",
        "initializing",
        "initialized",
        "game_playing",
        "main_menu",
        "game_ended",
        "quitting",
    ]

    transitions = [
        {"trigger": "initialize", "source": "unknown", "dest": "initializing"},
        {
            "trigger": "finish_initializing",
            "source": "initializing",
            "dest": "initialized",
        },
        {"trigger": "open_main_menu", "source": "initialized", "dest": "main_menu"},
        {"trigger": "open_main_menu", "source": "game_ended", "dest": "main_menu"},
        {"trigger": "start_game", "source": "main_menu", "dest": "game_playing"},
        {"trigger": "end_game", "source": "game_playing", "dest": "game_ended"},
        {"trigger": "quit", "source": "game_ended", "dest": "quitting"},
        {"trigger": "finish_quitting", "source": "quitting", "dest": "unknown"},
    ]

    def __init__(self):
        Machine.__init__(
            self,
            model=self,
            states=GameState.states,
            transitions=GameState.transitions,
            initial="unknown",
            auto_transitions=False,
            before_state_change="assign_prev_state",
            after_state_change="post_state_change",
        )
        self.prev_state = "unknown"

    def assign_prev_state(self):
        self.prev_state = self.state

    def post_state_change(self):
        pygame.event.post(
            pygame.event.Event(
                game_event.GAME_STATE_CHANGE,
                {"prev": self.prev_state, "current": self.state},
            )
        )
