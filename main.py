from curso import Curso
from estudiante import Estudiante

curso_uno = Curso(2210, "Programacion Avanzada", "Eder Rivera Cisneros")
curso_dos = Curso(2212, "Dinamica", "Jose Nicolas Ponciano")
curso_tres = Curso(2294,  "Calculo Integral", "Alejandro Aburto Bedolla")
estudiante_uno = Estudiante(10, "Tito",  21)
estudiante_dos = Estudiante(30, "Carlos", 20)  

estudiante_uno.agregar_curso(curso_uno)
estudiante_uno.agregar_curso(curso_dos)

estudiante_uno.mostrar_informacion_uno()

print("\n***************************")


estudiante_dos.agregar_curso_2(curso_dos)
estudiante_dos.agregar_curso_2(curso_tres)

estudiante_dos.mostrar_informacion_dos()
