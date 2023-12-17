import pandas as pd
import cv2

# data created by normalize_coordinates.py
data = "data.csv"

df = pd.read_csv(data)


X_0_IMG_DIR = "data_x_0/"
X_1_IMG_DIR = "data_x_1/"
Y_0_IMG_DIR = "data_y_0/"
Y_1_IMG_DIR = "data_y_1/"


# iterate through the directories and display the images
# for i in range(len(df)):

fname = "selection.csv"
f = open(fname, "w")
f.write("pixel,selection\n")

for i in range(len(df)):
    # x_0_img = cv2.imread(f"{X_0_IMG_DIR}pixel_{i}_x.png")
    # x_1_img = cv2.imread(f"{X_1_IMG_DIR}pixel_{i}_x.png")
    y_0_img = cv2.imread(f"{Y_0_IMG_DIR}pixel_{i}_y.png")
    y_1_img = cv2.imread(f"{Y_1_IMG_DIR}pixel_{i}_y.png")

    # display the images
    # cv2.imwrite("x_0.png", x_0_img)
    # cv2.imwrite("x_1.png", x_1_img)
    cv2.imwrite("y_0.png", y_0_img)
    cv2.imwrite("y_1.png", y_1_img)

    x = ""
    while x not in ["0", "1", "x", "q"]:
        x = input(
            "Enter 0 to select x_0, 1 to select x_1, x if neither, or q to quit: "
        )
        if x == "0":
            f.write(f"{i},0\n")
        elif x == "1":
            f.write(f"{i},1\n")
        elif x == "x":
            f.write(f"{i},x\n")
        elif x == "q":
            raise SystemExit
        else:
            print("Invalid input. Try again.")
