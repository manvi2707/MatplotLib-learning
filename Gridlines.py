import matplotlib.pyplot as plt
import numpy as np

# grid() => helps make plots easier to read by adding reference lines.

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 10, 15, 20, 25])

plt.grid(axis = "y",
         linewidth = 2,
         color="lightgrey",
         linestyle = "dashed")

plt.plot(x, y)

plt.show()