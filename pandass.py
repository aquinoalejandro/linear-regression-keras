import pandas as pd

# leo los datos
df = pd.read_csv("altura_peso.csv")

# pongo los datos en x e y
x = df["Altura"].values
y = df["Peso"].values



