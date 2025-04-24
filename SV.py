print("Bienvenid@")

# Solicitar de datos
Productos = []
Precios = []
PorcentajeDes = []
Cantidades = []  # Lista para almacenar la cantidad de cada producto
totalC = 0

# Bucle para agregar productos
while True:
    Producto = input("Ingrese el nombre del producto: ")
    Productos.append(Producto)

    # Solicitar y validar el precio unitario
    while True:
        precio_u = input(f"Ingrese el precio unitario del producto {Producto}: ")
        try:
            precio_u = float(precio_u)
            if precio_u > 0:
                Precios.append(precio_u)
                break
            else:
                print("El precio debe ser un valor positivo. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido para el precio.")

    # Solicitar y validar el porcentaje de descuento
    while True:
        pdesc = input(f"Ingrese el porcentaje de descuento para {Producto} (0-100): ")
        try:
            pdesc = float(pdesc)
            if 0 <= pdesc <= 100:
                PorcentajeDes.append(pdesc)
                break
            else:
                print("El descuento debe estar entre 0 y 100. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido para el descuento.")
    
    # Solicitar y validar la cantidad de cada producto
    while True:
        cantidad_producto = input(f"Ingrese la cantidad adquirida del producto {Producto}: ")
        try:
            cantidad_producto = int(cantidad_producto)
            if cantidad_producto > 0:
                Cantidades.append(cantidad_producto)
                break
            else:
                print("La cantidad debe ser un valor positivo. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido para la cantidad.")

    # Preguntar si desea agregar otro producto
    continuar = input("¿Desea agregar otro producto? (si/no): ").strip().lower()
    if continuar == "no":
        break

# Calcular el costo total
total_compra = 0
for i in range(len(Productos)):
    precio_con_descuento = Precios[i] * (1 - PorcentajeDes[i] / 100)
    total_producto = precio_con_descuento * Cantidades[i]
    total_compra += total_producto
    print(f"\nProducto: {Productos[i]}")
    print(f"Precio unitario: {Precios[i]:.2f}")
    print(f"Descuento aplicado: {PorcentajeDes[i]:.2f}%")
    print(f"Cantidad adquirida: {Cantidades[i]}")
    print(f"Precio final por producto: {precio_con_descuento:.2f}")
    print(f"Total por {Productos[i]}: {total_producto:.2f}")

# Mostrar el total de la compra
print(f"\nEl costo total de la compra es: {total_compra:.2f}")
