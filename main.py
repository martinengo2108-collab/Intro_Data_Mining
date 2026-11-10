import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer

breast_cancer = load_breast_cancer()

print("BREAST CANCER DATASET")
print(breast_cancer)

print("FEATURE NAMES :")
print(breast_cancer.feature_names)


print("TARGET NAMES :")
print(breast_cancer.target_names)

print("SHAPES :")
print(breast_cancer.data.shape)

df_breast=pd.DataFrame(
            breast_cancer.data,
                    columns=breast_cancer.feature_names
                    )
df_breast["target"]=breast_cancer.target

print(df_breast.head())