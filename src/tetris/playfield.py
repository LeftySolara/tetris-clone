import pygame


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
    def create(
        cls,
        pos: pygame.math.Vector2,
        side_length: int,
        filled: bool,
        groups: pygame.sprite._Group,
    ):
        """Factory method for creating playfield squares.

        Args:
            pos:
                The square's position on the screen.
            side_length:
                The length of each of the square's sides.
            filled:
                Whether a tetromino is occupying the square's space.
            groups:
                Pygame sprite groups to add the square to.

        Returns:
            PlayfieldSquare: An object representing one playfield square.
        """
        square = cls(groups)
        square.image = pygame.Surface((side_length, side_length))
        square.image.fill("Blue")

        square.rect = square.image.get_rect(topleft=pos)
        square.pos = pygame.math.Vector2(square.rect.topleft)
        square.filled = filled
        square.side_length = side_length

        return square


class Playfield(pygame.sprite.Sprite):
    """Area where tetrominos fall.

    Attributes:
        size: The size of the object's sprite rect.
        grid_rows: The number of rows in the grid.
        grid_cols: The number of columns in the grid.
        cells: A sprite group containing the grid squares.
    """

    size: pygame.math.Vector2
    grid_rows: int
    grid_cols: int
    cells: pygame.sprite.Group

    def __init__(
        self,
        pos: pygame.math.Vector2,
        rows: int,
        cols: int,
        square_length: int,
        groups: pygame.sprite._Group,
    ):
        super().__init__(groups)

        self.grid_rows = rows
        self.grid_cols = cols
        self.size = pygame.math.Vector2(
            square_length * self.grid_cols, square_length * self.grid_rows
        )

        self.image = pygame.Surface(self.size)
        self.image.fill("White")

        self.rect = self.image.get_rect(topleft=pos)

        self.cells = pygame.sprite.Group()

        for row in range(self.grid_rows):
            for col in range(self.grid_cols):
                pos = (col * square_length, row * square_length)
                PlayfieldSquare.create(pos, square_length, False, self.cells)
