class Calificaciones:
    def __init__(self, num_alumnos, num_materias):
        self.num_alumnos = num_alumnos
        self.num_materias = num_materias
        self.calificaciones = []
        self.nombres_materias = []

    def ingresar_calificaciones(self):
        self.nombres_materias = [input(f"Ingrese el nombre de la materia {i + 1}: ") for i in range(self.num_materias)]

        for i in range(self.num_alumnos):
            calificaciones_alumno = []
            print(f"\nIngresar calificaciones para el Alumno {i + 1}:")
            for j in range(self.num_materias):
                calificacion = float(input(f"Ingrese la calificación para {self.nombres_materias[j]}: "))
                calificaciones_alumno.append(calificacion)
            self.calificaciones.append(calificaciones_alumno)

    def mostrar_calificaciones(self):
        print("\nCalificaciones:")
        print("\t" + "\t".join(f"Alumno {i + 1}" for i in range(self.num_alumnos)))
        for j in range(self.num_materias):
            print(f"Materia {j + 1}:", end="\t")
            for i in range(self.num_alumnos):
                print(f"{self.calificaciones[i][j]}\t", end="")
            print()

    def buscar_calificacion(self, alumno, materia):
        if 1 <= alumno <= self.num_alumnos and 1 <= materia <= self.num_materias:
            return self.calificaciones[alumno - 1][materia - 1]
        else:
            return None

calificaciones_clase = Calificaciones(num_alumnos=100, num_materias=6)

calificaciones_clase.ingresar_calificaciones()

calificaciones_clase.mostrar_calificaciones()

alumno_buscar = int(input("\nIngrese el número de alumno a buscar (1-100): "))
materia_buscar = int(input("Ingrese el número de materia a buscar (1-6): "))

calificacion_buscada = calificaciones_clase.buscar_calificacion(alumno_buscar, materia_buscar)

if calificacion_buscada is not None:
    print(f"\nLa calificación del Alumno {alumno_buscar} en la Materia {materia_buscar} es: {calificacion_buscada}")
else:
    print(f"\nEl Alumno {alumno_buscar} o la Materia {materia_buscar} no existen en la matriz.")