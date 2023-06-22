import pygame
from dataclasses import dataclass
from tetris.state.game_state import GameState

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
            screen=None, screen_rect=SCREENRECT, fullscreen=fullscreen, state=None
        )
        game.init()
        return game

    def quit(self):
        pygame.quit()

    def start_game(self):
        self.state.start_game()
        self.loop()

    def loop(self):
        pass

    def init(self):
        """Initializes Pygame display and audio mixer."""

        pygame.init()

        self.state = GameState()
        self.state.initialize()

        window_style = pygame.FULLSCREEN if self.fullscreen else 0
        bit_depth = pygame.display.mode_ok(self.screen_rect.size, window_style, 32)
        screen = pygame.display.set_mode(self.screen_rect.size, window_style, bit_depth)
        pygame.display.set_caption("Tetris")

        pygame.mixer.pre_init(frequency=44100, size=32, channels=2, buffer=512)
        pygame.font.init()

        self.screen = screen

        self.state.finish_initializing()
