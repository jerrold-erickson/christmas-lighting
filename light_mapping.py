from image_processing import Camera_Manager, brightest_region
from led import LED_Manager

import time

COLOR_ON = (255, 255, 255)
BRIGHTNESS = 150
NUM_LIGHTS = 50

if __name__ == "__main__":
    camera = Camera_Manager()
    pixels = LED_Manager(n=NUM_LIGHTS, brightness=BRIGHTNESS)

    pixels.brightness = BRIGHTNESS

    for i in range(pixels.num_pixels):
        pixels[i] = COLOR_ON
        time.sleep(0.5)
        img = camera.capture()
        pixels[i] = (0, 0, 0)
        coords = brightest_region(img, save=True, save_name=f"data/pixel_{i}.png")
        print(f"Pixel {i}: {coords}")
