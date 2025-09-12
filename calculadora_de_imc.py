print("\n\n----------IMC------------\n\n") 

altura = float(input("introduzca su altura en metros: ")) 
peso = float(input("introduzca su peso en kg: ")) 

imc = peso/altura**2 
if imc < 18.5 : 
    print(f"su imc es {imc}, peso insuficiente ") 
elif imc >= 18.5 and imc <= 24.9 :
    print(f"au imc es {imc}, peso normal") 
elif imc >= 25.0 and imc <= 29.9 : 
    print(f"su imc es {imc}, sobrepeso") 
elif imc >= 30 and imc <= 34.9 : 
    print(f"su imc es {imc}, obesidad clase 1")
elif imc >= 35 and imc <= 39.9 : 
    print(f"su imc es {imc}, obesidad clase 2") 
else : 
    print(f"su imc es {imc}, obesidad clase 3 ") 