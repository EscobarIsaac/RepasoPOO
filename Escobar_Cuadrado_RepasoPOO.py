# Clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


# Clase Curso
class Curso:
    def __init__(self, nombre_curso):
        self.nombre_curso = nombre_curso
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_estudiantes(self):
        print(f"\nCurso: {self.nombre_curso}")
        print("Lista de estudiantes:")
        for estudiante in self.estudiantes:
            print(f"- {estudiante.mostrar_datos()}")


def main():
    # Crear estudiantes
    estudiante1 = Estudiante("Alejandro Cuadrado", 22)
    estudiante2 = Estudiante("Isaac Escobar", 23)
    curso_aplicaciones = Curso("Aplicaciones Distribuidas")
    curso_aplicaciones.agregar_estudiante(estudiante1)
    curso_aplicaciones.agregar_estudiante(estudiante2)
    curso_aplicaciones.mostrar_estudiantes()


if __name__ == "__main__":
    main()
