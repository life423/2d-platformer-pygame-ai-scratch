import os
import sys

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from gameplay.game_manager import Game

if __name__ == "__main__":
    game = Game()
    game.run()  # No arguments needed
