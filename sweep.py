import numpy as np
import pandas as pd
import itertools

from led import LED_Manager, COLORS

num_leds = 200

leds = LED_Manager(n=num_leds)

df = pd.read_csv("data.csv")
df = df.sort_values(by=["z"])

MAX_Z = df["z"].max()
SLICE_SIZE = 80
START = 130

colors = itertools.cycle(COLORS.values())

while True:
    min_z = START
    max_z = min_z + SLICE_SIZE

    while min_z < MAX_Z - SLICE_SIZE:
        color = next(colors)
        slice = df[(df["z"] > min_z) & (df["z"] < max_z)]
        for index, row in slice.iterrows():
            leds[row["led"]] = color

        min_z += SLICE_SIZE
        max_z += SLICE_SIZE
