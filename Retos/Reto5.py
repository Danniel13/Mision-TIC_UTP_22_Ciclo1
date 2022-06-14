
# #Descripción y requerimientos:
# Como consultor en recursos cinematográficos se le ha solicitado que organice la información necesaria que contenga:
# Entrada:
# Países (Country)
# Lengua Nativa (Language)
# Monto Bruto (Gross Earnings) en ganancias
# str
# str
# float
# Esto, con el fin de conocer los recursos que han salido de nuestro suelo y, en consecuencia, tomar en un futuro próximo la decisión de contratar recursos locales e iniciar la reactivación económica producto de la crisis pandémica
# En adición, usted cuenta con el archivo de datos “movies.csv” disponible desde:
# https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true
# En ese sentido, escriba una función que contenga la ruta de este archivo (descrita arriba) para su consulta y/o manipulación. A partir de estos datos, utilice los métodos pd.read_csv() y pivot_table()y cualquier otro método que ud. necesite para importar los datos del archivo .csv y crear una tabla dinámica en base a los datos solicitados, finalmente, mostrar los resultados finales.
# Salida:
# Tipo de retorno
# Descripción
# Lista
# Lista de valores indexados por ‘Country’ y ‘Languaje’ (Solo 10 registros) y la columna ‘Gross Earnings’
# Figura 1: Tabla resultados (Solo 10 registros del total)
import pandas as pd 




rutaFileCsv='https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'#Creación de variable con Link de csv
# def listaPeliculas()

def listaPeliculas(rutaFileCsv: str):

  # rutaFileCsv = pd.read_csv(rutaFileCsv)
  sp= rutaFileCsv.split("/") #Separación de caracteres de Link por "/"
  # print(sp[-1])
  if "csv" in sp[-1]:
    try:
      rd_csv = pd.read_csv(rutaFileCsv)#Lectura de archivo desde funcion!
      rd_csv_2= rd_csv[['Country','Language', "Gross Earnings"]] #Subconjunto de datos!
      # rd_csv_2=rd_csv.loc[0:9, ('Country','Language', "Gross Earnings")]
      gananciapaislanguage=rd_csv_2.pivot_table(index=['Country','Language'])#, column=['Country','Language','Gross Earnings'])#GENERACION DE TABLA DINAMICA
     
      return(gananciapaislanguage.head(10))#RETURN DE TABLA DINAMICA CON LOS PRIMEROS 10 REGISTROS
    except:
      return f"Error al leer el archivo de datos" #EXCEPT DE LECTURA DE DATOS

    # print(x.loc[0:9, ('Country','Language', "Gross Earnings")])
  else:
    return f"Extensión inválida."#RETURN DE EXTENSION INVALIDA 
  

print(listaPeliculas(rutaFileCsv))#OMITIR PRINT EN PLATAFORMA BOT