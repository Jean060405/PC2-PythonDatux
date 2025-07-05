lista = [{'nombre': 'oscar perez', 'notas': [12, 12, 12]},{'nombre': 'Cnady garcia ', 'notas': [13, 20, 14]}]

def promedio_curso(alumnos):
    total_promedios = 0
    for alumno in alumnos:
        promedio = sum(alumno['notas']) / len(alumno['notas'])
        total_promedios += promedio
    promedio_general = total_promedios / len(alumnos) if alumnos else 0
    return promedio_general
