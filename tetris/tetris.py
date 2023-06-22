import pygame
from dataclasses import dataclass
from game_state import GameState
from game_state import StateError

TARGET_FPS = 60
SCREENRECT = pygame.Rect(0, 0, 1024, 768)


@dataclass
class Tetris:
    screen: pygame.Surface
    screen_rect: pygame.Rect
    fullscreen: bool
    state: GameState

    @classmethod
    def create(cls, fullscreen=False):
        game = cls(
            screen=None,
            screen_rect=SCREENRECT,
            fullscreen=fullscreen,
            state=GameState.initializing,
        )
        game.init()
        return game

    def set_state(self, new_state: GameState):
        self.state = new_state

    def assert_state_is(self, *expected_states: GameState):
        if self.state not in expected_states:
            raise StateError(
                f"Expected the game state to be one of {expected_states} not {self.state}."
            )

    def quit(self):
        pygame.quit()

    def start_game(self):
        self.assert_state_is(GameState.initialized)
        self.set_state(GameState.main_menu)
        self.loop()

    def loop(self):
        while self.state != GameState.quitting:
            if self.state == GameState.main_menu:
                # pass control to game menu's loop
                pass
            elif self.state == GameState.game_playing:
                # ... etc ...
                pass
        self.quit()

    def init(self):
        """Initializes Pygame display and audio mixer."""
        self.assert_state_is(GameState.initializing)

        pygame.init()

        window_style = pygame.FULLSCREEN if self.fullscreen else 0
        bit_depth = pygame.display.mode_ok(self.screen_rect.size, window_style, 32)
        screen = pygame.display.set_mode(self.screen_rect.size, window_style, bit_depth)
        pygame.display.set_caption("Tetris")

        pygame.mixer.pre_init(frequency=44100, size=32, channels=2, buffer=512)
        pygame.font.init()

        self.screen = screen

        self.set_state(GameState.initialized)
