import cv2
import numpy as np
import time
import threading
import queue

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
    cv2.CAP_PROP_BUFFERSIZE: 1.0,
}

# image marker settings
M_COLOR = (0, 0, 255)
M_SIZE = 30
M_THICKNESS = 5


class Camera_Manager:
    def __init__(self, cam_settings: dict = CAM_SETTINGS):
        self._vc = cv2.VideoCapture(0)
        self._settings = cam_settings
        self.q = queue.Queue()

        # configure and open video capture
        for setting in self._settings:
            self._vc.set(setting, self._settings[setting])

        t = time.time()
        while not self._vc.isOpened():
            time.sleep(0.1)
            if time.time() - t > 5.0:
                raise RuntimeError("Failed to open camera.")

        self._t = threading.Thread(target=self._reader)
        self._t.daemon = True
        self._t.start()

    def __del__(self):
        self._t.join()
        self.vc.release()

    def _reader(self):
        while True:
            ret, frame = self._vc.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait()
                except queue.Empty:
                    pass
            self.q.put(frame)

    def capture(self):
        return self.q.get()


def brightest_region(
    image: np.ndarray,
    save: bool = False,
    save_name: str = "img.png",
    blur_size: int = 21,
):
    img_greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_greyscale = cv2.GaussianBlur(img_greyscale, (blur_size, blur_size), 0)
    *_, max_indx = cv2.minMaxLoc(img_greyscale)

    if save:
        cv2.drawMarker(image, max_indx, M_COLOR, cv2.MARKER_SQUARE, M_SIZE, M_THICKNESS)
        cv2.imwrite(save_name, image)

    return max_indx


if __name__ == "__main__":
    camera = Camera_Manager()

    while True:
        img = camera.capture()
        coords = brightest_region(img, save=True)
        print(f"Brightest region: {coords}")
