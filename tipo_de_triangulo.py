print("\n\n--------------------TIPO DE TRIANGULO----------------\n\n") 

lado1 = float(input("ingrese el primer lado: ")) 
lado2 = float(input("ingrese el segundo lado: ")) 
lado3 = float(input("ingrese el tercer lado: ")) 
if lado1 == lado2 and lado1 == lado3 : 
    print("es un triangulo equilatero") 
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
    print("es un triangulo isoceles") 
else : 
    print(" es un triangulo escaleno ") 
