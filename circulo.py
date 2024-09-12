class  Circulo:
    radio = 0
    area = 0
    perimetro = 0


    #Metodo constructor
    def __init__(self, radio):
        self.radio = radio

    def calcular_propiedades(self):
         variable_pi = 3.1416 
         self.area = variable_pi * self.radio * self.radio
         self.perimetro = variable_pi * self.radio * 2

         print("\nArea del circulo: ", self.area)
         print("\nPerimetro del circulo: ", self.perimetro)