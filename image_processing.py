import cv2


def brightest_region(image: str, gaussian_blur_size: int = 21) -> tuple:
    """Load image and find the coordinates of the brightest region.

    Args:
        image (str): Path to image.
        gaussian_blur_size (int, optional): Radius of applied gaussian blur. Defaults to 21.

    Returns:
        tuple: Coordinates of brightest region.
    """
    image_original = cv2.imread(image, cv2.IMREAD_COLOR)

    # convert to greyscale
    img_greyscale = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

    img_greyscale = cv2.GaussianBlur(
        img_greyscale, (gaussian_blur_size, gaussian_blur_size), 0
    )
    _, _, _, max_indx = cv2.minMaxLoc(img_greyscale)

    cv2.drawMarker(image_original, max_indx, (0, 0, 255), cv2.MARKER_SQUARE, 20, 2)

    cv2.imshow("Image", image_original)
    cv2.waitKey(0)


if __name__ == "__main__":
    img = "image.jpg"

    brightest_region(img)
