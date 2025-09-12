print("-----------EL MAYOR DE TRES NUMEROS--------") 

numero1 = float(input("\ningrese el primer numero: ")) 
numero2 = float(input("\ningrese el segundo numero: ")) 
numero3 = float(input("\ningrese el tercer numero: ")) 
if numero1 > numero2 and numero1 > numero3 : 
    print("el primer numero es el mayor") 
elif numero2 > numero1 and numero2 > numero3 : 
    print("el segundo numero es el mayor") 
else : 
    print("el tercer numero es el mayor")