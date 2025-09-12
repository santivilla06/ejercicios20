print("------------CALCULADORA DE AñO BISIESTO-----------") 

año = int(input("ingrese el año: ")) 

bisiesto = año % 4 == 0 and año % 100 != 0 
centenario = año % 400 == 0 
if bisiesto or centenario : 
    print(f'el año {año} es bisiesto') 
else : 
    print(f"el año {año} no es bisiesto") 