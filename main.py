from paciente.paciente import Paciente
from medico.medico import Medico
from hospital.hospital import Hospital

hospital = Hospital()

while True:

    print("BIENVENIDO AL SISTEMA DEL HOSPITAL")
    print("1.-Resgistrar paciente")
    print("2.-Registrar médico")
    print("3.-Mostrar pacientes")
    print("4.-Mostrar médicos")
    print("5.-Eliminar pacientes")
    print("6.-Eliminar médicos")
    print("7.-Mostrar pacientes menores de edad")
    print("8.-Mostrar pacientes mayores de edad")
    print("9.-Salir")

    opcion_usuario = input("Seleccione una opcion: ")

    if opcion_usuario == "1":
        print("Seleccionaste la opcion para registrar un paciente")
        
        nombre = input("Ingrese el nombre: ")
        ano_nacimiento = int(input("Ingrese el ano de nacimiento"))
        peso = float(input("Ingrese el peso: "))
        estatura = float(input("Ingrese el estatura: "))
        direccion = input("Ingrese el direccion: ")

    elif  opcion_usuario == "2":
        #registrar medico
        pass

    elif opcion_usuario == "3":
        hospital.mostrar_pacientes() 

    elif opcion_usuario == "4":
      hospital.mostrar_medicos()    

    elif opcion_usuario == "5":
      #eliminar paciente
      pass 

    elif opcion_usuario == "6":
      #Eliminar medico
      pass

    elif opcion_usuario == "7":
      #mostrar pacientes menores de edad
      pass 

    elif opcion_usuario == "8":
      #mostrar pacientes mayores de edad
      pass 

    elif opcion_usuario == "9":
      print("Hasta luego")
      break      