# --- Productos Disponibles ---
# Una lista de diccionarios que funciona como nuestro catálogo de productos.
productos = [
    {"nombre": "Manzana", "precio": 0.50},
    {"nombre": "Pan de molde", "precio": 2.50},
    {"nombre": "Leche (1L)", "precio": 1.20},
    {"nombre": "Docena de Huevos", "precio": 3.00},
    {"nombre": "Queso (250g)", "precio": 4.50},
    {"nombre": "Café (500g)", "precio": 5.75}
]

# --- Inicialización del Carrito ---
# Un diccionario para guardar los productos y sus cantidades.
carrito = {}

# --- Bucle principal del programa ---
# El programa se seguirá ejecutando hasta que el usuario elija la opción de salir.
while True:
    print("\n--- MENÚ DEL CARRITO DE COMPRAS ---")
    print("1. Ver productos disponibles")
    print("2. Agregar un producto al carrito")
    print("3. Ver mi carrito")
    print("4. Actualizar cantidad de un producto")
    print("5. Eliminar un producto del carrito")
    print("6. Salir")
    
    # Pedimos al usuario que elija una opción
    opcion = input("Por favor, elige una opción (1-6): ")

    # --- Opción 1: Ver productos ---
    if opcion == '1':
        print("\n--- Productos Disponibles ---")
        # Recorremos la lista de productos y la mostramos de forma ordenada
        for i, producto in enumerate(productos):
            print(f"  {i + 1}. {producto['nombre']} - ${producto['precio']:.2f}")
    
    # --- Opción 2: Agregar producto ---
    elif opcion == '2':
        print("\n--- Agregar Producto ---")
        # Mostramos la lista de productos para que el usuario elija
        for i, producto in enumerate(productos):
            print(f"  {i + 1}. {producto['nombre']} - ${producto['precio']:.2f}")
        
        try:
            seleccion = int(input("Ingresa el número del producto que quieres agregar: "))
            # Verificamos que el número esté en el rango correcto
            if 1 <= seleccion <= len(productos):
                producto_elegido = productos[seleccion - 1]
                nombre_producto = producto_elegido["nombre"]
                
                cantidad = int(input(f"¿Cuántas unidades de '{nombre_producto}' quieres agregar?: "))
                if cantidad > 0:
                    # Si el producto ya está en el carrito, sumamos la cantidad
                    if nombre_producto in carrito:
                        carrito[nombre_producto] += cantidad
                    # Si no, lo agregamos
                    else:
                        carrito[nombre_producto] = cantidad
                    print(f"¡{cantidad} x '{nombre_producto}' agregado(s) al carrito!")
                else:
                    print("Error: La cantidad debe ser mayor a cero.")
            else:
                print("Error: Número de producto no válido.")
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

    # --- Opción 3: Ver carrito ---
    elif opcion == '3':
        print("\n--- Tu Carrito de Compras ---")
        total = 0
        if not carrito:
            print("El carrito está vacío.")
        else:
            # Recorremos los items del carrito
            for nombre, cantidad in carrito.items():
                # Buscamos el precio del producto en nuestro catálogo
                precio_unitario = 0
                for producto in productos:
                    if producto["nombre"] == nombre:
                        precio_unitario = producto["precio"]
                        break
                
                subtotal = precio_unitario * cantidad
                total += subtotal
                print(f"- {nombre}: {cantidad} unidad(es) x ${precio_unitario:.2f} c/u = ${subtotal:.2f}")

            print("---------------------------------")
            print(f"TOTAL A PAGAR: ${total:.2f}")
            print("---------------------------------")

    # --- Opción 4: Actualizar cantidad ---
    elif opcion == '4':
        print("\n--- Actualizar Cantidad ---")
        if not carrito:
            print("El carrito está vacío, no hay nada que actualizar.")
        else:
            nombre_producto = input("Ingresa el nombre del producto que quieres actualizar: ")
            if nombre_producto in carrito:
                try:
                    nueva_cantidad = int(input(f"Ingresa la nueva cantidad para '{nombre_producto}': "))
                    if nueva_cantidad > 0:
                        carrito[nombre_producto] = nueva_cantidad
                        print(f"La cantidad de '{nombre_producto}' se actualizó a {nueva_cantidad}.")
                    elif nueva_cantidad == 0:
                        # Si la cantidad es 0, eliminamos el producto
                        del carrito[nombre_producto]
                        print(f"'{nombre_producto}' ha sido eliminado del carrito.")
                    else:
                        print("Error: La cantidad no puede ser negativa.")
                except ValueError:
                    print("Error: Ingresa una cantidad numérica válida.")
            else:
                print(f"Error: El producto '{nombre_producto}' no está en tu carrito.")

    # --- Opción 5: Eliminar producto ---
    elif opcion == '5':
        print("\n--- Eliminar Producto ---")
        if not carrito:
            print("El carrito está vacío, no hay nada que eliminar.")
        else:
            nombre_producto_eliminar = input("Ingresa el nombre del producto que quieres eliminar: ")
            if nombre_producto_eliminar in carrito:
                del carrito[nombre_producto_eliminar]
                print(f"'{nombre_producto_eliminar}' ha sido eliminado de tu carrito.")
            else:
                print(f"Error: El producto '{nombre_producto_eliminar}' no se encuentra en el carrito.")

    # --- Opción 6: Salir ---
    elif opcion == '6':
        print("\n¡Gracias por tu compra! Saliendo del programa...")
        break # Rompe el bucle while y termina el programa

    # --- Opción no válida ---
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")