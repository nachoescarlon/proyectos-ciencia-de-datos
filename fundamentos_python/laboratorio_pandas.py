import pandas as pd

datos_facultad = {
    "Materia": ["Algoritmos", "Álgebra", "Bases de Datos"],
    "Nota": [8, 2, 9]
}

tabla = pd.DataFrame(datos_facultad)

print("Nuestra tabla de la facultad:")
print(tabla)

promedio_pandas = tabla["Nota"].mean()
print("\nEl promedio calculado por la máquina es:", promedio_pandas)

tabla_aprobadas = tabla[tabla["Nota"] >= 4]

print("\nNuestra tabla filtrada (solo aprobadas):")
print(tabla_aprobadas)

promedio_real = tabla_aprobadas["Nota"].mean()
print("\nEl promedio real es:", promedio_real)