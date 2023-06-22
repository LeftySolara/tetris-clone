from tetris.tetris import Tetris


def start_game():
    game = Tetris.create()
    game.loop()


if __name__ == "__main__":
    start_game()
