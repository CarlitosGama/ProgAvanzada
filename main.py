from curso import Curso
from estudiante import Estudiante

estudiante = Estudiante(30, "Carlos", 20)
curso_uno = Curso(2210, "Programacion Avanzada", "Eder Rivera Cisneros")
curso_dos = Curso(2212, "Dinamica", "José Nicolas Ponciano")
curso_tres = Curso(2294,  "Calculo Integral", "Alejandro Aburto Bedolla")
estudiante_uno = Estudiante(10, "Tito",  21)
estudiante_dos = Estudiante(30, "Carlos", 20)  

estudiante.agregar_curso(curso_uno)
estudiante.agregar_curso(curso_dos)

estudiante.mostrar_informacion()

print("******************")


estudiante.agregar_curso(curso_dos)
estudiante.agregar_curso(curso_tres)

estudiante.mostrar_informacion()
