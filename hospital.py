class Hospital:
    pacientes = []
    medicos = []
    consulta = []

    
    def registar_consulta(self, id_paciente, id_medico):
      if not self.validar_cantidad_usuarios():
       return
      
      if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico):
         print("No se puede registrar la consulta, no existe el medico o el paciente")
         return
    
    def  mostrar_pacientes(self):
       print("*** Pacientes en el sistema ***")
       
          


    def validar_existencia_paciente(self, id_paciente):
       for paciente in self.pacientes:
          if paciente.id ==id_paciente:
             return True
       return False
    
    def validar_existencia_medico(self, id_medico):
       for medico in self.medicos:
          if medico.id ==id_medico:
             return True
       return False
      


    def validar_cantidad_usuarios(self):
        if(len(self.pacientes)) == 0:
         print("No puedes registrar una consulta, no hay pacientes")
         return False
        

        if len(self.medicos) == 0:
            print("No puedes registrar una consulta, no existen medicos")
            return False
        
        return True