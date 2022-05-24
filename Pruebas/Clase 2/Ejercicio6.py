#Ejercicio 6
# Análisis del problema
# ¿Qué me pide el problema?
# PRECIO DEL PRODUCTO ANTES DE DESCUENTO
# ¿Qué datos necesito?
# VALOR PRODUCTO CON DESCUENTO
# DESCUENTO
# FORMULA
# ¿Cómo debo responder?
# EL PRECIO TOTAL DEL PRODUCTO SIN DESCUENTO

#PROCEDIMIENTO:
#Dividir descuento entre 100: 15/100= 0.15
#Restar 1 del porcentaje de descuento: 1-0.15 =0.85
#Dividir valor producto con descuento / 0.85 = 40
#Valor real sin descuento

Valor_pant_desc= 34
descuento = 15
Valor1 = (1- (descuento /100) )

print(Valor1)

print("El valor sin descuento es", Valor_pant_desc / Valor1, "€")
