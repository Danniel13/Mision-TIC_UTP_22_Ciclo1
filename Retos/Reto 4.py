
# RETO 4
# Descripción del problema:
# Un contador necesita llevar una bitácora acerca de los registros diarios de una papelería, en consecuencia,
# esta información que necesita automatizar es la siguientes:
# Entrada:
# Número de orden Código del producto Cantidad Precio unitario
# int de 4 a 6 dígitos str de 4 a 6 dígitos Int Float
# Salida:
# Tipo de retorno Descripción
# Str Cadena de caracteres de la forma:
# “La factura <número> tiene un total en pesos de <cantidad>”
# Requerimiento.


def ordenes(rutinaContable):
  from functools import reduce
  compra_minima= 600000 #Revisar con "Orden_minima"

  #Declaración primeras lambdas: sacar valores totales  de cada orden: multiplicacion de cantidad por valor
  TotalOC = list(map(lambda x: [x[0]] + list(map(lambda y:y[1] * y[2], x[1:])), rutinaContable))#x toma el valor de la lista de tuplas: para este caso: [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], el mas es para concaterar el 1201 con los respectivos valores las tuplas
  #"Y" toma el elemento 1 de la lista * el elemento 2 de la lista en este caso Para el caso de la primera tupla: 4* 25842.99

  #_________________________________________________________________________________________
  #
  # print(TotalOC)

  TotalOC = list(map(lambda x: [x[0]] + [reduce(lambda a,b:round(a+b,2), x[1:])], TotalOC))#Lista el numero de pedido y el valor total sumado de todos los productos de cada tupla(pedido)
  # print(TotalOC)

  TotalOC = list(map(lambda x : x if x [1] >= compra_minima else (x[0], x[1] + 25000), TotalOC))#Hace lo mismo que el codigo anterior pero con una condicion de que si el pedido no cumple con el monto minimo estipulado en la variable compra_minima entonces que sume 25000 al total
  # print(TotalOC)

  print('----------------- Inicio Registro diario --------------------------')
  for x in range(len(TotalOC)):#Recorrido de la totalOC para proceder a generar los diferentes print:
     #print("La factura",TotalOC[x][0], "tiene un total en pesos de", TotalOC[x][1])  "NO PONE COMA "
     print(f"La factura {TotalOC[x][0]} tiene un total en pesos de {TotalOC[x][1]:,.2f}") #Es valido por que pone la coma como lo pide el bot
  print('----------------- Fin Registro diario -----------------------------')


rutinaContable = [
[1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
[1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
[1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
[1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]


ordenes(rutinaContable)