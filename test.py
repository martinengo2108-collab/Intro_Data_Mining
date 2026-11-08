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

sns.set_theme(style="darkgrid")
sns.regplot(x="Heures_Etudes", y="Note_Examen", data=df, color="blue")

plt.title("Relation entre les heures d'études et la note d'examen")
plt.xlabel("Heures d'études")
plt.ylabel("Note d'examen")
plt.show()