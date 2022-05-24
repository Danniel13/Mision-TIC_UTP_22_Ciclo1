#Ejercicio 5
# Estás interesado en comprarte un nuevo PC y en la tienda 
# de tu barrio cuesta 660€ con todos los accesorios incluídos. Sin embargo, el vendedor te descuenta el 10% por pronto pago ¿Cuánto tienes que pagar en total por el ordenador con todos los accesorios?

# Análisis del problema
# ¿Qué me pide el problema?
# Cual es el pago total de PC

# ¿Qué datos necesito?
# Valor total
# Porcentaje de descuento
# Total Descuento
# Total valor de PC con descuentos
# Si se va a realizar el pago con pronto pago o no para aplicar
# descuento.


# ¿Cómo debo responder?
# Se realiza un algoritmo con la toma de variables correspondientes
# a los valores del producto y descuento, se requiere saber
# si se va a emplear un medio de pago especifico para realizar
# el descuento.

costo_PC = 660
descuento_PC = 10
Descuento_total= costo_PC * descuento_PC /100
precio_total = costo_PC - Descuento_total 
print(Descuento_total)


pago =input("Digite SI en caso de realizar pronto pago ")
if pago == "SI":
  print ("El valor a pagar es: ",  precio_total, "€")
else:
  print("El valor a pagar es: ", costo_PC, "€")
