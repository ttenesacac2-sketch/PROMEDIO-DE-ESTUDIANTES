
 # 1. Definición de la función lambda para calcular el promedio
# Toma una lista de notas, suma sus valores, los divide por el número de notas
# y redondea el resultado a 2 decimales.
calcular_promedio = lambda notas: round(sum(notas) / len(notas), 2)

# 2. Diccionario de estudiantes y sus notas (la estructura de datos)
estudiantes = {
    "Estudiante1": [8, 8.5, 7],
    "Estudiante2": [10, 8, 9.5],
    "Estudiante3": [10, 9, 9],
    "Estudiante4": [7, 8.5, 8],
    "Estudiante5": [10, 8, 10],
    "Estudiante6": [5, 6, 7],
    "Estudiante7": [8, 9.5, 9],
    "Estudiante8": [7, 7, 8],
    "Estudiante9": [9, 9, 10],
    "Estudiante10": [6, 6, 7],
    "Estudiante11": [10, 10, 9.5],
    "Estudiante12": [9, 9, 8],
}

# 3. Mostrar la cabecera del resultado en formato de tabla
# El método .center() y los f-strings con alineación (< para izquierda, > para derecha)
# se usan para crear la tabla.

print("\n" + " PROMEDIOS DE LOS ESTUDIANTES ".center(40, "="))
print(f'{"Nombre":<20}{"Promedio":>10}')
print("=" * 30)

# 4. Bucle para iterar y mostrar los resultados
for nombre, notas in estudiantes.items():
    # Se llama a la función lambda 'calcular_promedio' con la lista de notas
    promedio_final = calcular_promedio(notas)

    # Se imprime el nombre (alineado a la izquierda en 20 espacios) y
    # el promedio (alineado a la derecha en 10 espacios, con 2 decimales fijos)
    print(f"{nombre:<20}{promedio_final :>10.2f}")

print("=" * 30) 
