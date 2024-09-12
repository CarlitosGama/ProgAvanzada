class Estudiante:

    id_estudiante = 0
    nombre = ""
    edad = 0

    cursos = []
    
    #constructor dela clase estudiante
    def __init__(self, id_estudiante, nombre, edad):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.edad = edad

     #Agregar cursos
    def agregar_curso(self, curso):
        self.cursos.append(curso)

    #Mostrar informacion
    def mostrar_informacion(self, estudiante):
        print("\n----- Informacion del Estudiante ------\n")

        print("\n")
        print(estudiante.id_estudiante)
        print(estudiante.nombre)
        print(estudiante.edad) 

        if  len(self.cursos) == 0:
            print("No existen productos en el sistema")
            return

        for curso in self.cursos:
            print("\n")
            print(curso.codigo_curso)
            print(curso.nombre_curso)
            print(curso.instructor)         
    
