def calcular_promedio(notas):
    return sum(notas) / len(notas) if notas else 0

def main():
    estudiantes = {
        "Estudiante1": [5, 8, 9, 9],
        "Estudiante2": [9, 6, 9, 10],
        "Estudiante3": [9, 9, 5, 8],
        "Estudiante4": [7, 9, 8, 8],
        "Estudiante5": [9, 9, 7, 10],
        "Estudiante6": [10, 8, 9, 7],
        "Estudiante7": [9, 9, 10, 10],
        "Estudiante8": [8, 5, 10, 10],
        "Estudiante9": [7, 9, 9, 6],
        "Estudiante10": [9, 10, 9,  8],
        "Estudiante11": [10, 7, 10, 9],
        "Estudiante12": [5, 9, 10, 6],
    }

    print("Promedios de los estudiantes:")
    for nombre, notas in estudiantes.items():
        print(f"{nombre}: {calcular_promedio(notas):.2f}")

if __name__ == "__main__":
    main()
