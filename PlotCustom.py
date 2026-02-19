import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])

line_style = dict(marker=".",
            markersize = 30,
            markerfacecolor="pink",
            markeredgecolor="pink",
            linestyle="solid",
            linewidth="2",)

plt.plot(x, y1, color="#1e57ba", **line_style) # markersize=>ms, markerfacecolor => mfc, markeredgecolor => mec
plt.plot(x, y2, color="green", **line_style) # to astricks are to unpack line_style dictionary
plt.plot(x, y3, color="red", **line_style)

plt.show() 