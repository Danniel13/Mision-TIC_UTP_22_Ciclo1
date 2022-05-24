num_1 = input("Ingrese el primer número:")
num_2 = input("Ingrese el segundo número:")

print(type(num_1), type(num_2))

#Conversión de variable a tipo INT para operaciones
num_1 = int(float(num_1))
num_2 = int(float(num_2))

print(type(num_1), type(num_2))

print(num_1, "*", num_2, "=", num_1 * num_2)