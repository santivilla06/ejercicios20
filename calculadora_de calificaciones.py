print("\n\n--------------CALCULADORA DE CALIFICACIONES-------------\n\n") 

nota = int(input("\ningres la nota: ")) 
if nota < 0 or nota > 100 : 
    print("\nerror introduce una nota valida (0-100)\n") 
elif nota >= 90 : 
    print("\ntu nota es A\n") 
elif nota >= 80 : 
    print("\ntu nota es B\n") 
elif nota >= 70 : 
    print("\ntu nota es C") 
elif nota >= 60 : 
    print("\ntu nota es D") 
else : 
    print("\ntu nota es F")