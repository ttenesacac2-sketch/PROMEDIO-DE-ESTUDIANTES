# promedio_notasestudiantes.py
def calcular_promedio(notas):
    return sum(notas) / len(notas) if notas else 0
notas_estudiantes={
    "Estudiante1":[5,7,9],
    "Estudiante2":[8,9,8],
    "Estudiante3":[6,7,8],
    "Estudiante4":[9,5,10],
    "Estudiante5":[7,8,9],
    "Estudiante6":[7,7,7],
    "Estudiante7":[10,9,10],
    "Estudiante8":[5,6,6],
    "Estudiante9":[8,8,8],
    "Estudiante10":[4,8,7],
    "Estudidante11":[9,9,9],
    "Estudiante12":[9,8,10],
}
def calcular_promedios_estudiantes(notas_estudiantes):
    return sum(notas_estudiantes) / len(notas_estudiantes if notas_estudiantes else 0)
for estudiante, notas in notas_estudiantes.intems():
    promedio=calcular_promedio(notas)
    print(f"{estudiante}: {promedio:.2f}")