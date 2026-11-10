import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris

iris=load_iris()

print("IRIS FLOWER DATASET")

print("Features :")
print(iris.feature_names)

print("Target Names :")
print(iris.target_names)