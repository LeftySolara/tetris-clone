import enum


class GameState(enum.Enum):
    """Enum for the game's state machine."""

    """Unknown state, indicating possible error or misconfiguration."""
    unknown = "unknown"

    """The state the game engine would rightly be set to before
    anything is initialized or configured."""
    initializing = "initializing"

    """The game engine is initialized: pygame is configured, the sprite
    images are loaded, etc."""
    initialized = "initialized"

    """The game engine is in game playing mode."""
    game_playing = "game_playing"

    """The game engine is in the main menu."""
    main_menu = "main_menu"

    """The game engine is rendering the game ended screen."""
    game_ended = "game_ended"

    """The game engine is exiting and is unwinding."""
    quitting = "quitting"


class StateError(Exception):
    """An error in the game's state.

    This is raised if the game is in an unexpected game state at a point
    where we expect it to be in a different state. For instance, to
    start the game loop we must be initialized.
    """
