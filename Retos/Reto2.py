
# #Esta función debe retornar un nuevo diccionario con las llaves nombre,
# edad, atracción, primer_ingreso, total_boleta y apto del cliente:
# • En donde apto tendrá como valor una variable booleana, será verdadera
# si su edad cumple con los rangos exigidos en la tabla anterior, en el
# caso contrario será falsa.
# • En el caso de atraccion y total_boleta, si no se cumple el rango de
#  edades se le asignara un valor de ‘N/A’ a cada uno.
# • Si primer_ingreso es verdadero, el total_boleta será el valor
#  de la boleta menos el descuento de lo contrario se pagará el valor
#  neto de la boleta.

datos = {
  "id_cliente": int, 
  "nombre": str, 
  "edad": int, 
  "primer_ingreso": bool,
}
#print(datos)
#datos["id_cliente"]="00100"
#datos["nombre"]="Robertinho"
#print(datos)





datos["id_cliente"] ="00100"
datos["nombre"] ="Tatiana Ruiz"
datos["edad"] =7
datos["primer_ingreso"] = False
#NOTA1: IMPORTANTE: NO ES NECESARIO CREAR UN SEGUNDO DICCIONARIO SE PUEDE USAR EL PRIMERO Y SE VAN AGREGANDO LOS ELEMENTOS
#QUE NO ESTAN DEFINIDOS INICIALMENTE COOMO SON: APTO Y TOTAL BOLETA


#Definición diccionario de salida(NO ES NECESARIO SE PUEDE USAR EL PRIMERO Y AGREGAR ELEMENTOS, VER NOTA1)
Diccionario ={
  "nombre": datos["nombre"],
  "edad": datos["edad"],
  "atraccion": str,
  "apto": bool, 
  "primer_ingreso": datos["primer_ingreso"],
  "Total_boleta": int,
  

}



#Definir condiciones!!!!


if (datos["edad"]) >= 7:
  Diccionario["apto"] = True
else: 
  Diccionario["apto"] = False 
  
if (datos["edad"]) < 7:
  Diccionario["atraccion"] = "N/A"
  Diccionario["Total_boleta"] = "N/A"

if datos["primer_ingreso"] == True and datos["edad"] >18:
  Diccionario["Total_boleta"] = 20000 -1000
  Diccionario["atraccion"] = "X-Treme"
elif datos["primer_ingreso"] ==False and datos["edad"] >18:
  Diccionario["Total_boleta"] = 20000
  Diccionario["atraccion"] = "X-Treme"
  
if datos["edad"] >= 15 and datos["edad"] <= 18 and datos["primer_ingreso"] ==True:
  Diccionario["Total_boleta"] = 5000 -350
  Diccionario["atraccion"] = "Carros chocones"
elif datos["primer_ingreso"] ==False and datos["edad"] >= 15 and datos["edad"] <= 18:
  Diccionario["Total_boleta"] = 5000
  Diccionario["atraccion"] = "Carros chocones"

if datos["primer_ingreso"] ==True and datos["edad"] >= 7 and datos["edad"] < 15:
  Diccionario["Total_boleta"] = 10000 -500
  Diccionario["atraccion"] = "Sillas voladoras"
elif datos["primer_ingreso"] ==False and datos["edad"] >= 7 and datos["edad"] < 15:
  Diccionario["Total_boleta"] = 10000
  Diccionario["atraccion"] = "Sillas voladoras"


print(Diccionario)
 
  
  

 
  
  


  

    
  

 