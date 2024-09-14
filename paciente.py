import random

class  Paciente:
    id = 0
    nombre = ""
    ano_nacimiento = 0
    peso = 0
    estatura = 0
    direccion = ""

    def __init__(self, nombre, ano_nacimiento, peso, estatura, direccion):
      self.id = random.randint(1, 1000)
      self.nombre = nombre
      self.ano_nacimiento = ano_nacimiento 
      self.peso = peso
      self.estatura = estatura
      self.direccion = direccion


    def mostrar_informacion(self):
        for paciente in self.pacientes:
          print(f"\nId: {paciente.id}")
          print(f"\nNombre: {paciente.nombre}")
          print(f"\nPeso: {paciente.peso}")
          print(f"\nEstatura: {paciente.estatura}")
          print(f"\nDireccion: {paciente.direccion}")