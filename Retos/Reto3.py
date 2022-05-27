# Descripción del problema:
# Una venta de autopartes necesita de forma urgente un registro de partes vendidas a diferentes compradores,
# motivo por el cual, se hace necesario en el futuro inmediato registrar dichas ventas y que las mismas puedan
# ser consultadas por un tipo particular de producto, para ello, la información introducida debe ser la siguiente:


# Entradas: Lista de tuplas
# Nombre Abreviación Tipo Descripción
# IdProducto N/A Int Identificador único del producto
# dProducto N/A Char Descripción del producto
# pnProducto N/A Char Numero de parte del producto
# cvProducto N/A Int Cantidad vendida del producto
# sProducto N/A Int Stock del producto
# nComprador N/A Char Nombre del comprador
# cComprador N/A Int Documento de identidad del comprador
# fVenta N/A Char Fecha de venta del producto


# Salida: diccionario con lista de tuplas
# Tipo de retorno Descripción
# Str {:} Cadena de caracteres de la forma
# Producto consultado : {idProducto} Descripción {dProducto}
# #Parte {pnProducto} Cantidad vendida {cvProducto} Stock
# {sProducto} Comprador {nComprador} Documento
# {cComprador} Fecha Venta {fVenta}
# Ó
# “No hay registro de venta de ese producto”




def AutoPartes(ventas:list): 
    venta = {}
    for idProducto, dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas:
        if venta.get(idProducto) == None:
           venta[idProducto] = []
        venta[idProducto].append((dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta))
    return venta


def consultaRegistro(ventas,idProducto):
    if idProducto in ventas:
        for dProducto, pnProducto, cvProducto, sProducto, nComprador, cComprador, fVenta in ventas[idProducto]:
            #print ("Producto consultado :", idProducto , "Descripción" , dProducto , "#Parte" , pnProducto , "Cantidad vendida" , cvProducto , "Stock" , sProducto , "Comprador" , nComprador , "Documento" , cComprador , "Fecha Venta" , fVenta)
            print("Producto consultado :",idProducto ,  " Descripción " ,  dProducto ,  " #Parte " ,  pnProducto ,  " Cantidad vendida " ,  cvProducto ,  " Stock " ,  sProducto , " Comprador" , nComprador ,  " Documento " ,  cComprador ,  " Fecha Venta " ,  fVenta)
    else:
        print("No hay registro de venta de ese producto")


consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),    
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
