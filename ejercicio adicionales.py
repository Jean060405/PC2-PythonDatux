def cargar_alumnos():
    alumnos = []
        n = int(input("Ingrese la cantidad de alumnos: "))
        return []
    for i in range(n):
        print(f"Alumno {i + 1}:")
        nombre = input("Ingrese el nombre completo del alumno: ").strip()
        notas = []
        for j in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j} (0 a 10): "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("La nota debe estar entre 0 y 10.")
                except ValueError:
                    print("Ingrese un número válido.")

        alumno = {"nombre": nombre, "notas": notas}
        alumnos.append(alumno)
    return alumnos
