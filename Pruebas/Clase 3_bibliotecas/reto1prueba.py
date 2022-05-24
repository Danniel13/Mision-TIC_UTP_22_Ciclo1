capital = 650000
tiempo= 2
if tiempo > 2:
    porcentaje_interes = 0.03
    Valor_intereses= (capital  * porcentaje_interes * tiempo / 12)
    valor_total = (Valor_intereses + capital)
    
else:
    porcentaje_interes = 0.02
    Valor_intereses= (capital * porcentaje_interes)
    valor_total = int(capital - Valor_intereses)
    

print(valor_total)