# promedio_notas.py
# Calcular promedio de 12 estudiantes

notas_estudiantes = {
    "Estudiante1":  [10, 9, 8, 7, 9],
    "Estudiante2":  [9, 8, 7, 6, 8],
    "Estudiante3":  [8, 7, 9, 6, 10],
    "Estudiante4":  [7, 6, 8, 9, 7],
    "Estudiante5":  [10, 10, 9, 8, 9],
    "Estudiante6":  [9, 7, 8, 6, 7],
    "Estudiante7":  [6, 7, 8, 7, 6],
    "Estudiante8":  [10, 9, 9, 8, 10],
    "Estudiante9":  [8, 7, 6, 9, 8],
    "Estudiante10": [9, 10, 8, 9, 7],
    "Estudiante11": [7, 8, 6, 7, 8],
    "Estudiante12": [10, 9, 10, 8, 9],
}

def calcular_promedio(notas):
    return sum(notas) / len(notas)

print("PROMEDIOS DE LOS 12 ESTUDIANTES\n")
for estudiante, notas in notas_estudiantes.items():
    promedio = calcular_promedio(notas)
    print(f"{estudiante}: {promedio:.2f}")
