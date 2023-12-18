import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
x_sel = pd.read_csv("x_selection.csv")
y_sel = pd.read_csv("y_selection.csv")

x_sel = x_sel.drop(columns=["pixel"])
y_sel = y_sel.drop(columns=["pixel"])

# combine the dataframes

df = pd.concat([df, x_sel, y_sel], axis=1)

# for each row where x_sel is 1, replace x_0 with x_1 and z_x_0 with z_x_1
df.loc[df["x_sel"] == 1, "x_0"] = df["x_1"]
df.loc[df["x_sel"] == 1, "z_x_0"] = df["z_x_1"]

# for each row where y_sel is 1, replace y_0 with y_1 and z_y_0 with z_y_1
df.loc[df["y_sel"] == 1, "y_0"] = df["y_1"]
df.loc[df["y_sel"] == 1, "z_y_0"] = df["z_y_1"]

# drop the cols we don't need anymore
df.drop(columns=["x_sel", "y_sel"], inplace=True)
df.drop(columns=["x_1", "z_x_1", "y_1", "z_y_1"], inplace=True)

# normalze z values from 0
min_z = min(df["z_x_0"].min(), df["z_y_0"].min())
df["z_x_0"] -= min_z
df["z_y_0"] -= min_z

# drop the _0 from the column names
df = df.rename(columns={"x_0": "x", "z_x_0": "z_x", "y_0": "y", "z_y_0": "z_y"})

# average the z values
df["z"] = df[["z_x", "z_y"]].mean(axis=1).astype(int)

# drop the z_x and z_y columns
df.drop(columns=["z_x", "z_y"], inplace=True)

# name the index led
df = df.rename(columns={"Unnamed: 0": "led"})

BAD_LEDS = 14, 192, 195

# for each bad LED, average the neighboring x, y and z coordinates
for led in BAD_LEDS:
    neighbors = df.loc[df["led"] == led + 1, ["x", "y", "z"]].values[0]
    neighbors += df.loc[df["led"] == led - 1, ["x", "y", "z"]].values[0]

    neighbors = [int(x / 2) for x in neighbors]

    df.loc[df["led"] == led, ["x", "y", "z"]] = neighbors

df.to_csv("filtered_data.csv", index=False)
