from typing import Tuple
from pydantic import BaseSettings


class GameWindowSettings(BaseSettings):
    # Window
    CELL_WIDTH: int = 9
    CELL_HEIGHT: int = 9
    CELL_MARGIN: int = 1
    FONT: str = "Arial"
    CAPTION: str = "Conway's Game of Life - Cellular Automaton"


class Colors(BaseSettings):
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    GRAY: Tuple[int, int, int] = (50, 50, 50)
    WHITE: Tuple[int, int, int] = (255, 255, 255)
