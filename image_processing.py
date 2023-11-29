import cv2
import numpy as np
from datetime import datetime

CAM_SETTINGS = {
    cv2.CAP_PROP_FOURCC: cv2.VideoWriter_fourcc(*"MPJG"),
    cv2.CAP_PROP_FRAME_WIDTH: 1920.0,
    cv2.CAP_PROP_FRAME_HEIGHT: 1080.0,
    cv2.CAP_PROP_FPS: 5.0,
    cv2.CAP_PROP_BRIGHTNESS: 0.0,
    cv2.CAP_PROP_CONTRAST: 17.0,
    cv2.CAP_PROP_SATURATION: 10.0,
    cv2.CAP_PROP_HUE: 0.0,
    cv2.CAP_PROP_GAIN: -1.0,
}

# image marker settings
M_COLOR = (0, 0, 255)
M_SIZE = 30
M_THICKNESS = 5


def brightest_region(image: np.ndarray, blur_size: int = 21):
    img_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_greyscale = cv2.GaussianBlur(img_greyscale, (blur_size, blur_size), 0)
    *_, max_indx = cv2.minMaxLoc(img_greyscale)
    cv2.drawMarker(image, max_indx, M_COLOR, cv2.MARKER_SQUARE, M_SIZE, M_THICKNESS)

    filename = f"{datetime.now().strftime('%m-%d_%H-%M-%S')}.png"
    cv2.imwrite(filename, image)


def capture_image():
    capture = cv2.VideoCapture(0)

    for setting in CAM_SETTINGS:
        capture.set(setting, CAM_SETTINGS[setting])

    if not capture.isOpened():
        print("Failed to open camera.")
        return

    rval, frame = capture.read()
    if not rval:
        print("Failed to capture image.")
        return

    capture.release()
    return frame


if __name__ == "__main__":
    img = capture_image()
    brightest_region(img)
