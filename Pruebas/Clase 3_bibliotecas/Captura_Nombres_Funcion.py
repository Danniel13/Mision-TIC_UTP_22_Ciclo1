def recibir_nombre(numero): #Donde numero es la variable que se va a pedir.


  """Captura por teclado de nombre y apellidos."""
  
  nombre= input("Ingrese su primer nombre" + str(numero) + ": ")
  Apellido= input("Ingrese su primer apellido" + str(numero) + ": ")

  return nombre + " " + Apellido


nombre_completo = recibir_nombre(1)
print(nombre_completo)
    
    