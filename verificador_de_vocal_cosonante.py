print("\n\n---------------VERIFICADOR DE VOCAL O CONSONANTE----------------\n\n") 

caracter = input("ingresa una letra: ").upper() 
if len(caracter) == 1 and caracter.isalpha(): 
    if caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U" : 
        print("\nla letra es una vocal") 
    else : 
        print("\nla letra es una consonante") 
else : 
    print("\ndebe introducir solo un caracter y debe ser del alfabeto")    