import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    "Heures_Etudes": [1, 2, 3, 4, 5],
    "Note_Examen": [60, 70, 80, 90, 100]
}
df = pd.DataFrame(data)

print("--Apercu de nos donnees")
print(df)