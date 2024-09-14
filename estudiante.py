class Estudiante:

    id_estudiante = 0
    nombre = ""
    edad = 0
    cursos_uno = []
    cursos_dos = []
    
    #constructor de la clase estudiante
    def __init__(self, id_estudiante, nombre, edad):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.edad = edad

     #Agregar cursos al estudiante 1
    def agregar_curso(self, curso):
        self.cursos_uno.append(curso)
     
     #Agregar cursos al estudiante 2
    def agregar_curso_2(self, curso):
        self.cursos_dos.append(curso)

    #Mostrar informacion estudiante 1
    def mostrar_informacion_uno(self):
        print("\n----- Informacion del Estudiante ------\n")

        print("\n")
        print(self.id_estudiante)
        print(self.nombre)
        print(self.edad) 

        if  len(self.cursos_uno) == 0:
            print("No existen cursos registrados")
            return

        for curso in self.cursos_uno:
            print("\n")
            print(curso.codigo_curso)
            print(curso.nombre_curso)
            print(curso.instructor)         
   
    #Mostrar informacion estudiante 2
    def mostrar_informacion_dos(self):
        print("\n----- Informacion del Estudiante ------\n")

        print("\n")
        print(self.id_estudiante)
        print(self.nombre)
        print(self.edad) 

        if  len(self.cursos_dos) == 0:
            print("No existen cursos registrados")
            return

        for curso in self.cursos_dos:
            print("\n")
            print(curso.codigo_curso)
            print(curso.nombre_curso)
            print(curso.instructor)         
