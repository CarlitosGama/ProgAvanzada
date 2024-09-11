class Coche:
    id = 0
    marca = ""
    modelo = ""
    año = 0
    edad = 0
#Metodo Constructor
    def __init__(self, id, marca, modelo, año):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.año = año

#Metodo para mostrar la informacion de los productos
    def mostrar_informacion(self):
        print("\n----- Informacion del producto ------\n")

        print("Id: ", self.id)
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Año: ", self.año)

    def calcular_edad(self):
        año_actual = 2024
        self.edad = año_actual - self.año
        print("Edad del coche: ", self.edad)

