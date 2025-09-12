print("\n\n-------------MENU-------------\n\n") 

print("\n a continuacion se le mostrara algunas opciones del menu para que eliga ") 

menu = input("\n1.PAPAS FRITAS.\n2.PIZZA.\n3.PERRO CALIENTE.\n\nelija una opcion:  ").upper() 
if menu == "PAPAS" or menu == "1" : 
    print("\nsus papas va en camino\n") 
elif menu == "PIZZA" or menu == "2" : 
    print("\nsu pizza va en camino\n") 
else : 
    print("su perro va en camino.") 