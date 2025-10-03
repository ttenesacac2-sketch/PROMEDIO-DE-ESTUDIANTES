# PROMEDIO-DE-ESTUDIANTES
REPOSITORIO PARA CALCULAR PROMEDIO DE NOTAS
Versión interactiva para ejecutar localmente
n_students = 5
students = {}
for i in range(n_students):
    name = input(f"Nombre del estudiante {i+1}: ")
    grades_str = input("Introduce las notas separadas por comas (ej. 85,90,78): ")
    grades = [float(g.strip()) for g in grades_str.split(',') if g.strip() != ""]
    students[name] = grades

# Luego reutiliza la m# Calcular promedio con función lambda
promedio = lambda notas: round(sum(notas) / len(notas), 2) if notas else 0

# Diccionario de estudiantes y sus notas
estudiantes = dict([
    ("Estudiante1", [8, 9, 7]),
    ("Estudiante2", [7, 6, 8]),
    ("Estudiante3", [10, 9, 9]),
    ("Estudiante4", [5, 5, 6]),
    ("Estudiante5", [10, 8, 10]),
    ("Estudiante6", [5, 6, 7]),
    ("Estudiante7", [8, 8, 9]),
    ("Estudiante8", [7, 7, 8]),
    ("Estudiante9", [9, 8, 10]),
    ("Estudiante10", [6, 6, 7]),
    ("Estudiante11", [10, 10, 9]),
    ("Estudiante12", [8, 9, 8]),
])

# Mostrar resultados en forma de tabla
print("Promedios de los estudiantes".center(40, "-"))
print(f"{'Nombre':<15}{'Promedio':>10}")
print("-" * 25)

for nombre, notas in estudiantes.items():
    print(f"{nombre:<15}{promedio(notas):>10.2f}")
 
