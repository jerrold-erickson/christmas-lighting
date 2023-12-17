import board
import neopixel
import random
import time
import numpy as np


class LED_Manager:
    DEFAULT_LEDS = 50
    DEFAULT_BRIGHTNESS = int(0.3 * 255)

    def __init__(
        self, n: int = DEFAULT_LEDS, brightness: int = DEFAULT_BRIGHTNESS
    ) -> None:
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
        assert value in range(10, 256), "Brightness must be in range [10, 255]."

        self._brightness = value
        for i in range(self._num_pixels):
            self[i] = self[i]

    def random(self) -> None:
        colors = (
            np.random.dirichlet(np.ones(3), size=self._num_pixels) * self._brightness
        )
        for i in range(self._num_pixels):
            self[i] = colors[i]


if __name__ == "__main__":
    num_leds = 200
    brightness = 125
    pixels = LED_Manager(n=num_leds, brightness=brightness)

    # pixels.off()

    length = int(num_leds * 0.8)

    for head in range(length):
        color = np.random.dirichlet(np.ones(3)) * 255
        pixels[head] = color
        time.sleep(0.05)

    head += 1
    tail = head - length

    while True:
        color = np.random.dirichlet(np.ones(3)) * 255
        pixels[head] = color
        pixels[tail] = (0, 0, 0)
        time.sleep(0.05)

        head += 1
        tail += 1

        if head == num_leds:
            head = 0
        if tail == num_leds:
            tail = 0
