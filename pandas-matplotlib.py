import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("data.csv")

group = df.groupby("Type1")
type_count = group["No"].count().sort_values()
# OR print(df["Type1"].value_counts(ascending=True))

plt.barh(type_count.index, type_count.values, color="skyblue",
         edgecolor="blue")
plt.title("# of Pokemon of Primary Type")
plt.xlabel("Count")
plt.ylabel("Type")
plt.tight_layout()
plt.show()