num_alumnos = 5
num_materias = 10

calificaciones = [[0] * num_materias for _ in range(num_alumnos)]

for i in range(num_alumnos):
    print(f"Ingrese las calificaciones del alumno {i+1}: ")
    for j in range(num_materias):
        calificacion = float(input(f"Calificación en materia {j+1}: "))
        calificaciones[i][j] = calificacion

print("\nCalificaciones ingresadas: ")
for i in range(num_alumnos):
    print(f"Alumno {i+1}: {calificaciones[i]} ")

alumno_buscado = int(input("Ingrese el número de alumno a buscar (1-5): ")) - 1
materia_buscada = int(input("Ingrese el número de materia a buscar (1-10): ")) - 1

if 0 <= alumno_buscado < num_alumnos and 0 <= materia_buscada < num_materias:
    calificacion_buscada = calificaciones[alumno_buscado][materia_buscada]
    print(f"La calificación del alumno {alumno_buscado + 1} en la materia {materia_buscada + 1} es: {calificacion_buscada} ")
else:
    print("Los números de alumno y materia deben estar entre 1 y 10. ")