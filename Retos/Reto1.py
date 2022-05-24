#ofrece rendimientos a una tasa fija, asegurando una rentabilidad libre de riesgo en un 
#tiempo determinado que por lo general debe ser mayor a dos (2) meses. Si, este dinero se 
#retira antes de este periodo se aplica una penalidad del 2%.
#En ese sentido, el valor de los intereses ganados por un periodo de tiempo superior a dos meses 
# se determina a través de la siguiente formula:
#1111!
#2222!
# #Donde:
# cantidad = dinero ingresado en el CDT
# procentajea perder = 2% (0.02)
# En consecuencia, el valor total del dinero será calculado a través de la siguiente formula
#valor_total_perd= cantidad - valor_perdido

#DEFINICION DE FUNCION:
def CDT(usuario: str, capital: int, tiempo: int):
  #Primer condicional para evaluar Ganancias de cdt si tiempo es >2 se aplicara la formula de hallar 
  #el valor de los intereses,
  #y el valor total que es los intereses + el capital
  if tiempo > 2:
    porcentaje_interes = 0.03
    Valor_intereses= (capital  * porcentaje_interes * tiempo) / 12
    valor_total = (Valor_intereses + capital)
    #else para definir el CDT en caso de que sea menor o igual a dos meses entonces se aplicara un regargo con 
    #la formula a continuacion
  else:
    porcentaje_interes = 0.02
    Valor_intereses= (capital * porcentaje_interes)
    valor_total = capital - Valor_intereses

  #Return con la información Output
  return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"
  
    
#print(f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}")
print(CDT("AB1012",650000,2))#PRINT Para sacar la informacion del return con datos establecidos.





  #porcentaje_interes = 0.03 

  

#donde:
# Donde:
# capital = dinero ingresado en el CDT
# porcentaje_interes = 3% (0.03).
# tiempo = cantidad de tiempo

#En consecuencia, el valor total del dinero será calculado a través de la siguiente formula:
  
#Se debe determinar el valor total a retirar por el cliente que invirtió en el CDT al final del periodo.


#Por otra parte, para un periodo de tiempo inferior o igual a dos meses se debe aplicar
#la siguiente formula:
  
  