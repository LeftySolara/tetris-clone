import pygame
from dataclasses import dataclass
from tetris.state import GameState

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


@dataclass
class Game:
    """Game management class.

    This class is a container for all of the various game elements.
    It manages the screen, mixer, clock, and game state, along with
    the main game loop.
    """

    screen: pygame.Surface
    state: GameState

    @classmethod
    def create(cls):
        """Factory method for creating and initializing a Game object.

        Returns:
            Game: The game object.
        """
        game = cls(screen=None, state=GameState())
        game.init()

        return game

    def init(self):
        """Initialize Pygame display and audio mixer."""

        pygame.init()
        self.state.initialize()

        bit_depth = pygame.display.mode_ok((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, bit_depth)
        pygame.display.set_caption("Tetris")

        pygame.mixer.pre_init(frequency=44100, size=32, channels=2, buffer=512)
        pygame.font.init()

        self.screen = screen

        self.state.finish_initializing()

    def quit(self):
        pygame.quit()
