import matplotlib.pyplot as plt
import numpy as np

# Scatter Graph => Shows the relation between two variable
#                  Helps to identify a correlation (+, -, None)
#                  Example: Study hours vs Test Scores

x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) # Hour studied
y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]) # Grades

x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8]) # Hour studied
y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97]) # Grades

plt.scatter(x1, y1, color="skyblue",
                  alpha = 0.5,
                  s = 200,
                  label = "Class A")

plt.scatter(x2, y2, color="pink",
                  alpha = 0.5,
                  s = 200,
                  label = "Class B")

plt.legend() # to show which color represent which classes data

plt.xlabel("Hours studied")
plt.ylabel("Grade")
plt.title("Test Scores")

plt.show()