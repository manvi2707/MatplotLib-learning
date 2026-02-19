import matplotlib.pyplot as plt
import numpy as np

# Histogram => A visual representation of distribution of quantitative data
#              They group values into bins (intervals)
#              and counts how many fall into each range.

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100) # clip(array, min_value, max_value) provide range of values for array
# loc means location of the median of data. here scores will revolve around 80
# scale means standard deviation. how far are scores gonna divert from the centre

plt.hist(scores, bins=10,
                 color="lightgreen",
                 edgecolor="black")

plt.title("Exam scores")
plt.xlabel("Score")
plt.ylabel("No. of students")
plt.show()
