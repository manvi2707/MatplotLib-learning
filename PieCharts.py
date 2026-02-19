import matplotlib.pyplot as plt
import numpy as np

# Pie Chart => Circular chart divided into slices to show percentages of the total.
#              Good for visualizing distribution among categories.

categories = np.array(["Freshmen", "Sophomores", "Juniors", "Seniors"])
values = np.array([300, 250, 275, 225])
colour = np.array(["pink", "skyblue", "#d10676", "#19b1ac"])

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                colors=colour,
                explode = [0, 0, 0, 0.1],
                shadow = True,
                startangle = 90) # explode means to seperate the slices. 

plt.title("College")

plt.show()