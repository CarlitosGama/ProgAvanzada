class Curso:
    codigo_curso = 0
    nombre_curso = ""
    instructor = ""

    def __init__(self, codigo_curso, nombre_curso,  instructor):
        self.codigo_curso = codigo_curso
        self.nombre_curso = nombre_curso
        self.instructor = instructor

    def mostrar_info_curso(self):
    
        print("\n", self.codigo_curso)
        print("\n", self.nombre_curso)
        print("\n", self.instructor)