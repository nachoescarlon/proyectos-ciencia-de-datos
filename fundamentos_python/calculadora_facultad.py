notas = [8, 2, 9]

suma_total = 0
materias_aprobadas = 0

for nota in notas:
    if nota < 4:
        print("Se detectó un aplazo con nota:", nota)
    else:
        print("Materia aprobada con:", nota)
        suma_total = suma_total + nota
        materias_aprobadas = materias_aprobadas + 1

promedio = suma_total / materias_aprobadas
print("Tu promedio de materias aprobadas es:", promedio)