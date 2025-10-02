def calcular_promedio(notas):
    return sum(notas) / len(notas) if notas else 0

def main():
    estudiantes = {
        "Estudiante1": [8, 9, 7],
        "Estudiante2": [7, 6, 8],
        "Estudiante3": [9, 10, 9],
        "Estudiante4": [6, 7, 8],
        "Estudiante5": [10, 9, 10],
        "Estudiante6": [5, 6, 7],
        "Estudiante7": [8, 8, 9],
        "Estudiante8": [7, 7, 6],
        "Estudiante9": [9, 8, 10],
        "Estudiante10": [6, 5, 7],
        "Estudiante11": [10, 10, 9],
        "Estudiante12": [8, 9, 8]
    }

    print("Promedios de los estudiantes:")
    for nombre, notas in estudiantes.items():
        print(f"{nombre}: {calcular_promedio(notas):.2f}")

if __name__ == "__main__":
    main()
