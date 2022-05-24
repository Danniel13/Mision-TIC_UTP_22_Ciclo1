i = 1
while i <= 3:
    print(i)
    i += 1
print("Programa terminado")
print()



#La ventaja de un bucle while es que la variable de control se puede modificar con mayor flexibilidad, 
#Como en el ejemplo siguiente:
while i <= 50:
    print(i)
    i = 3 * i + 1
print("Programa terminado")

print()

# Otra ventaja del bucle while es que el número de iteraciones no está definida antes de empezar el bucle, 
# por ejemplo porque los datos los proporciona el usuario. Por ejemplo, el siguiente ejemplo pide un número 
# positivo al usuario una y otra vez hasta que el usuario lo haga correctamente:
numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración")