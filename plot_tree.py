import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = "filtered_data.csv"

df = pd.read_csv(data)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

for i in range(len(df)):
    x = df["x"][i]
    y = df["y"][i]
    z = df["z"][i]
    ax.scatter(x, y, z, c='r', marker='o')

plt.show()