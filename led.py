import board
import neopixel
import time
import numpy as np

COLORS = {
    "RED": (0, 182, 0),
    "GREEN": (251, 55, 0),
    "BLUE": (55, 0, 251),
    "ORANGE": (101, 233, 0),
    "WHITE": (219, 240, 77),
}


class LED_Manager:
    DEFAULT_LEDS = 50

    def __init__(self, n: int = DEFAULT_LEDS, brightness: float = 0.1) -> None:
        self._leds = neopixel.NeoPixel(board.D18, n, brightness=brightness)
        self._n = n

    @property
    def num_LEDs(self) -> int:
        return self._n

    @property
    def brightness(self) -> float:
        return self._leds.brightness

    @brightness.setter
    def brightness(self, value: float) -> None:
        self._leds.brightness = value

    def fill(self, color: tuple) -> None:
        assert len(color) == 3, "Color must be a tuple of length 3."
        self._leds.fill(color)

    def __getitem__(self, index: int) -> tuple:
        return self._leds[index]

    def __setitem__(self, index: int, color: tuple) -> None:
        assert len(color) == 3, "Color must be a tuple of length 3."

        self._leds[index] = color

    def off(self) -> None:
        self.fill((0, 0, 0))

    def random(self) -> None:
        colors = np.random.dirichlet(np.ones(3), size=self._n) * 255
        for i in range(self._n):
            self[i] = colors[i]


if __name__ == "__main__":
    num_leds = 200
    brightness = 0.3
    LED = LED_Manager(n=num_leds, brightness=brightness)

    length = int(num_leds * 0.8)

    for head in range(length):
        color = (np.random.dirichlet(np.ones(3)) * 255).astype(int)
        LED[head] = color

    head += 1
    tail = head - length

    while True:
        color = (np.random.dirichlet(np.ones(3)) * 255).astype(int)
        LED[head] = color
        LED[tail] = (0, 0, 0)
        time.sleep(0.02)

        head += 1
        tail += 1

        if head == num_leds:
            head = 0
        if tail == num_leds:
            tail = 0
