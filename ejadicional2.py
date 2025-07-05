[{'nombre': 'oscar perez', 'notas': [12, 12, 12]},{'nombre': 'Cnady garcia ', 'notas': [13, 20, 14]}]
def evaluar_aprobacion(alumnos):
    aprobados = 0
    desaprobados = 0
    for alumno in alumnos:
        promedio = sum(alumno['notas']) / len(alumno['notas'])
        if promedio >= 4:
            aprobados += 1
        else:
            desaprobados += 1
    return aprobados, desaprobados
