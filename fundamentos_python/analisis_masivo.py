import pandas as pd

dataset = pd.read_csv("peliculas_limpias.csv")

dimensiones = dataset.shape
print("El tamaño de nuestro dataset es:", dimensiones)

print("\nPrimeras 5 películas cargadas:")
print(dataset.head())

promedio_ganancia = dataset["ganancia"].mean()
print("\nEl promedio histórico de ganancia por película es:", promedio_ganancia)