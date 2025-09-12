print("\n\n---------------CALCULADORA DE DESCUENTO-------------\n") 
 
print("por un monto mayor a 100$, se establece 15% de descuento\n") 

cuenta = float(input("ingrese el monto establecido: ")) 

descuento = cuenta - (cuenta * 0.15) 
if cuenta > 100 : 
    print("\ntiene un descuento del 15%,tu monto a pagar es:" , descuento ) 
else : 
    print("tu monto es menor a 100, no tienes el descuento") 
     