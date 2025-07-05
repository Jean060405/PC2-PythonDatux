#pregunta 4
alumnos = []

n = int(input("¿Cuántos alumnos desea registrar?: "))

for i in range(n):
    print(f"Alumno {i + 1}")
    nombre = input("Nombre del alumno: ")
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {j + 1} de {nombre}: "))
                if 0 <= nota <= 20:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 20.")
            except ValueError:
                print("Debe ingresar un número válido.")
    alumno = {"Alumno": nombre,"Notas": notas}
    alumnos.append(alumno)
for a in alumnos:
    print(f"Alumno: {a['Alumno']}, Notas: {a['Notas']}")