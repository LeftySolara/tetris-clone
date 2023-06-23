import pygame
from dataclasses import dataclass


@dataclass
class PlayfieldSquare(pygame.sprite.Sprite):
    """A single square in the playfield.

    Attributes:
        side_length (int): The length of each side of the square.
        filled (bool): Whether a tetromino is occupying the square's space.
    """

    side_length: int
    filled: bool

    def __init__(self, groups: pygame.sprite._Group):
        super().__init__(groups)

    @classmethod
    def create(cls, pos, side_length, filled, groups):
        """Factory method for creating playfield squares.

        Returns:
            PlayfieldSquare: An object representing one playfield square.
        """
        square = cls(groups)
        square.image = pygame.Surface((side_length, side_length))
        square.image.fill("White")

        square.rect = square.image.get_rect(topleft=pos)
        square.pos = pygame.math.Vector2(square.rect.topleft)
        square.filled = filled
        square.side_length = side_length

        return square
