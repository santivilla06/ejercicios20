print("\n---------- Calculadora de Costo de Envio ----------")
print("\nDescuento del 10% en envios superiores a 5 kilogramos\n")
print("\nZonas de destinos disponibles:\n")
print("1: America del sur.\n2: America del norte.\n3: Europa.")

'''Tabla de Costos por Zona y Peso:
Zona 1: América del Sur
* Menos de 1 kg: $10.00
* Entre 1 kg y 5 kg: $15.00
*Más de 5 kg: $20.00
Zona 2: América del Norte
*Menos de 1 kg: $18.00
*Entre 1 kg y 5 kg: $25.00
*Más de 5 kg: $30.00
Zona 3: Europa
*Menos de 1 kg: $24.00
*Entre 1 kg y 5 kg: $35.00
*Más de 5 kg: $45.00'''

zona = int(input("\nIntroduce el numero de la zona de destino: "))
peso = float(input("\nIntroduce el peso en kilogramos: "))

costo_base = 0
costo_final = 0 
descuento = 0

if zona == 1:
    if peso > 0 and peso < 1:
        costo_base = 10.00
    elif peso >= 1 and peso <= 5:
        costo_base = 15.00
    elif peso > 5:
        costo_base = 20.00
    else:
        print("Error: el peso debe ser mayor a cero")
elif zona == 2:
    if peso > 0 and peso < 1:
        costo_base = 18.00
    elif peso >= 1 and peso <= 5:
        costo_base = 25.00
    elif peso > 5:
        costo_base = 30
    else:
        print("Error: el peso debe ser mayor a cero")
elif zona == 3:
    if peso > 0 and peso < 1:
        costo_base = 24
    elif peso >= 1 and peso <= 5:
        costo_base = 35
    elif peso > 5:
        costo_base = 45
    else:
        print("Error: el peso debe ser mayor a cero")

'''Regla de Descuento:
Si el paquete pesa más de 5 kg, se aplica un 10% de descuento sobre el costo base para incentivar envíos grandes'''

if costo_base > 0:
    costo_final = costo_base
        
    if peso > 5:
        descuento = costo_base * 0.10
        costo_final = costo_base - descuento
        print(f"\nCosto Base: ${costo_base}")
        print(f"Descuento por paquete pesado (10%): -${descuento}\n")

        print(f"El costo final del envio es: ${costo_final}") 
    else:
        print(f"No obtienes descuento, tu monto a cancelar es ${costo_base}")