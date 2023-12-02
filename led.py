import board
import neopixel
import random
import time
import numpy as np


NUM_LEDS = 50
DEFAULT_BRIGHTNESS = int(0.1 * 255)


class LED_Manager:
    def __init__(self, n: int = NUM_LEDS, brightness: int = DEFAULT_BRIGHTNESS) -> None:
        self._leds = neopixel.NeoPixel(board.D18, n)
        self._num_pixels = n
        self.brightness = brightness

    @property
    def num_pixels(self) -> int:
        return self._num_pixels

    def fill(self, color: tuple) -> None:
        assert len(color) == 3, "Color must be a tuple of length 3."
        self._leds.fill(color)

    def __getitem__(self, index: int) -> tuple:
        return self._leds[index]

    def __setitem__(self, index: int, color: tuple) -> None:
        assert len(color) == 3, "Color must be a tuple of length 3."
        s = max(sum(color), 1)
        color = [int((c / s) * self._brightness) for c in color]

        self._leds[index] = color

    def off(self) -> None:
        self.fill((0, 0, 0))

    @property
    def brightness(self) -> int:
        return self._brightness

    @brightness.setter
    def brightness(self, value: int) -> None:
        assert value in range(10, 255), "Brightness must be in range [10, 255]."

        self._brightness = value
        for i in range(self._num_pixels):
            self[i] = self[i]

    def random(self) -> None:
        colors = np.random.dirichlet(np.ones(3), size=NUM_LEDS) * self._brightness
        for i in range(self._num_pixels):
            self[i] = colors[i]


if __name__ == "__main__":
    pixels = LED_Manager()

    pixels.random()
