class Hospital:
    pacientes = []
    medicos = []
    consulta = []

    
    def registar_consulta(self):
       self.validar_cantidad_usuarios()


    def validar_cantidad_usuarios(self):
        if(len(self.pacientes)) == 0:
         print("No puedes registrar una consulta, no hay pacientes")
         return
        

        if len(self.medicos) == 0:
            print("No puedes registrar una consulta, no existen medicos")
            return