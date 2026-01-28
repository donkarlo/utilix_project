from utilix.data.kind.graphic.color.color import Color
from typing import Tuple

class RgbAlpha(Color):
    def __init__(self, red: int, green: int, blue: int, alpha: float):
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    def get_red_green_blue_alpha(self) -> Tuple[int, int, int, float]:
        return (self._red, self._green, self._blue, self._alpha)
