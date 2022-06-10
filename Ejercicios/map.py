# def doblar(X):
#   return X*2

from ast import comprehension


num=[2, 3, 5, 7, 20, 50]
a=[1, 2, 3, 4, 5]
b=[6, 7, 8, 9, 10,]


# #Map reemplaza el for hace el proceso automatizado.
# print(map(doblar, num))#Genera un iterable de tipo map, algo que no se puede ver./Se hizo pero no se refleja
# print(list(map(doblar, num))) #Generacion MAP con LISTA

#LAMBDA:

# print(list(map(lambda x: x*2, num)))  


#LAMBDA DE MULTIPLICACION DE DOS LISTAS:VARIABLES LOCALES DE LAMBDA: X Y: OPERACION XY Y LUEGO DEFINIR LAS GLOBALES A Y B
lista_Res=(list(map(lambda x,y:x*y,a,b)))


print(lista_Res)

 
#CONVERSION A LISTA DE TUPLAS:
#____________________________
# tuplist= list(zip(lista_Res))
# print(tuplist)
#_____________________________




print([x*y for x,y in zip(a,b)])#->list comprehension