from image_processing import Camera_Manager, brightest_region
from led import LED_Manager

import time

COLOR_ON = (255, 255, 255)
BRIGHTNESS = 80
NUM_LIGHTS = 200

if __name__ == "__main__":
    camera = Camera_Manager()
    LED = LED_Manager(n=NUM_LIGHTS, brightness=BRIGHTNESS)

    LED.brightness = BRIGHTNESS

    data = {}

    for i in range(LED.num_LEDs):
        LED[i] = COLOR_ON
        time.sleep(0.5)
        img = camera.capture()
        LED[i] = (0, 0, 0)
        coords = brightest_region(img, save=True, save_name=f"data/pixel_{i}_y.png")
        print(f"Pixel {i}: {coords}")

        data[i] = coords

    fname = "data/y_coords.csv"
    with open(fname, "w") as f:
        f.write("index,x,y\n")
        for i in range(LED.num_LEDs):
            f.write(f"{i},{data[i][0]},{data[i][1]}\n")
