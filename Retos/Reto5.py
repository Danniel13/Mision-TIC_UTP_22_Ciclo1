from operator import index
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
  

(listaPeliculas(rutaFileCsv))