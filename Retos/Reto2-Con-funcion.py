informacion = { 
  "id_cliente": int, 
  "nombre": str, 
  "edad": int, 
  "primer_ingreso": bool,
}

#Definicion de Función:
def cliente (informacion:dict): 
  
  #Validación de edad inicial:
  if (informacion["edad"]) >= 7:
    informacion["apto"] = True
  else: 
    informacion["apto"] = False 
  #Validacion 2 de edad inicial:  
  if (informacion["edad"]) < 7:
    informacion["atraccion"] = "N/A"
    informacion["total_boleta"] = "N/A"
  #Validación de condiciones segun rango de edad para darle salida al total de la boleta:
  if informacion["primer_ingreso"] == True and informacion["edad"] >18:
    informacion["total_boleta"] = float(20000 -1000)
    informacion["atraccion"] = "X-Treme"
  elif informacion["primer_ingreso"] ==False and informacion["edad"] >18:
    informacion["total_boleta"] = 20000
    informacion["atraccion"] = "X-Treme"
    
  if informacion["edad"] >= 15 and informacion["edad"] <= 18 and informacion["primer_ingreso"] ==True:
    informacion["total_boleta"] = float(5000 -350)
    informacion["atraccion"] = "Carros chocones"
  elif informacion["primer_ingreso"] ==False and informacion["edad"] >= 15 and informacion["edad"] <= 18:
    informacion["total_boleta"] = 5000
    informacion["atraccion"] = "Carros chocones"

  if informacion["primer_ingreso"] ==True and informacion["edad"] >= 7 and informacion["edad"] < 15:
    informacion["total_boleta"] = float(10000 -500)
    informacion["atraccion"] = "Sillas voladoras"
  elif informacion["primer_ingreso"] ==False and informacion["edad"] >= 7 and informacion["edad"] < 15:
    informacion["total_boleta"] = 10000
    informacion["atraccion"] = "Sillas voladoras"

  #Orden de print y return para validar funcion:
  print({"nombre":informacion["nombre"] , "edad":informacion["edad"] , "atraccion":informacion["atraccion"] , "apto":informacion["apto"] , "primer_ingreso":informacion["primer_ingreso"] , "total_boleta":informacion["total_boleta"]})
  return {"nombre":informacion["nombre"] , "edad":informacion["edad"] , "atraccion":informacion["atraccion"] , "apto":informacion["apto"] , "primer_ingreso":informacion["primer_ingreso"] , "total_boleta":informacion["total_boleta"]}
  

  #Llamado de funcion con diferentes valores
cliente(informacion = { "id_cliente": 10001, "nombre": "Johana Fernandez","edad": 20,"primer_ingreso": True,})
cliente(informacion = { "id_cliente": 10001, "nombre": "Johana Fernandez","edad": 20,"primer_ingreso": False,})
cliente(informacion = { "id_cliente": 10001, "nombre": "Gloria Suarez","edad": 3,"primer_ingreso": True,})
cliente(informacion = { "id_cliente": 10001, "nombre": "Tatiana Suarez","edad": 17,"primer_ingreso": True,})
cliente(informacion = { "id_cliente": 10001, "nombre": "Tatiana Suarez","edad": 17,"primer_ingreso": False,})
cliente(informacion = { "id_cliente": 10001, "nombre": "Tatiana Ruiz","edad": 8,"primer_ingreso": True,})
cliente(informacion = { "id_cliente": 10001, "nombre": "Tatiana Ruiz","edad": 8,"primer_ingreso": False,})
cliente(informacion = { "id_cliente": 10001, "nombre": "Tatiana Ruiz","edad": 2,"primer_ingreso": False,})
cliente(informacion = { "id_cliente": 10001, "nombre": "Tatiana Ruiz","edad": 81,"primer_ingreso": True,})