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

print("Shapes :")
print(iris.data.shape)

df_iris=pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df_iris["target"]=iris.target
print(df_iris.head())