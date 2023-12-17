import pandas as pd


RES_WIDTH = 1920
RES_HEIGHT = 1080
X_1_OFFSET = 70
Y_1_OFFSET = 67


def x_1_norm(x):
    return (RES_WIDTH - x) + X_1_OFFSET


def y_1_norm(y):
    return (RES_WIDTH - y) + Y_1_OFFSET


def z_norm(z):
    return RES_HEIGHT - z


x_0_data = "data_x_0/x_coords.csv"
x_1_data = "data_x_1/x_coords.csv"
y_0_data = "data_y_0/y_coords.csv"
y_1_data = "data_y_1/y_coords.csv"


x_0_df = pd.read_csv(x_0_data)
x_1_df = pd.read_csv(x_1_data)
y_0_df = pd.read_csv(y_0_data)
y_1_df = pd.read_csv(y_1_data)

x_0_df = x_0_df.drop(columns=["index"])
x_1_df = x_1_df.drop(columns=["index"])
y_0_df = y_0_df.drop(columns=["index"])
y_1_df = y_1_df.drop(columns=["index"])

# x data: rename x to x_0 and x_1 and y to z_x_0 and z_x_1
x_0_df = x_0_df.rename(columns={"x": "x_0"})
x_1_df = x_1_df.rename(columns={"x": "x_1"})
x_0_df = x_0_df.rename(columns={"y": "z_x_0"})
x_1_df = x_1_df.rename(columns={"y": "z_x_1"})

# y data: rename x to y_0 and y_1 and y to z_y_0 and z_y_1
y_0_df = y_0_df.rename(columns={"x": "y_0"})
y_1_df = y_1_df.rename(columns={"x": "y_1"})
y_0_df = y_0_df.rename(columns={"y": "z_y_0"})
y_1_df = y_1_df.rename(columns={"y": "z_y_1"})

# combine the dataframes
df = pd.concat([x_0_df, x_1_df, y_0_df, y_1_df], axis=1)

# normalize the data
df["x_1"] = df["x_1"].apply(x_1_norm)
df["z_x_0"] = df["z_x_0"].apply(z_norm)
df["z_x_1"] = df["z_x_1"].apply(z_norm)
df["y_1"] = df["y_1"].apply(y_1_norm)
df["z_y_0"] = df["z_y_0"].apply(z_norm)
df["z_y_1"] = df["z_y_1"].apply(z_norm)


# save the data
df.to_csv("data.csv", index=True)