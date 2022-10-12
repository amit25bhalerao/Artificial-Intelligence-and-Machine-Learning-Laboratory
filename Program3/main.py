import pandas as pd
import numpy as np

# Reading Data From Input File
data = pd.read_csv("Data.csv")
print(data)

# Creating An Array Of Attributes
d = np.array(data)[:, : -1]
print("\nAttributes\n", d)

# Segregating The Target That Has Positive And Negative Examples
target = np.array(data)[:, -1]
print("\nTarget\n", target)


# Training Function To Implement Find-S Algorithm
def train(c, t):
    for i, val in enumerate(t):
        if val == "Yes":
            specific_hypothesis = c[i].copy()
            generic_hypothesis = [["?" for i in range(len(specific_hypothesis))] for i in range(len(specific_hypothesis))]
            break

    for i, val in enumerate(c):
        if t[i] == "Yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                    generic_hypothesis[x][x] = '?'
                else:
                    pass

        if t[i] == "No":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    generic_hypothesis[x][x] = specific_hypothesis[x]
                else:
                    generic_hypothesis[x][x] = '?'

    return generic_hypothesis


# Obtaining The Final Hypothesis
print("\nFinal Hypothesis\n", train(d, target))