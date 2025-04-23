print("Bienvenid@")
#Solicitar de datos

Productos=[]
Precios=[]
PorcentajeDes=[]

Cantidad=input("Ingrese la cantidad de productos adquiridos ")
Cantidad=int(Cantidad)

for x in range (Cantidad):
    Producto=input("Ingrese el nombre del producto ")
    Productos.append(Producto)
    PrecioU=input("Ingrese el precio unitario ")
    PrecioU=float(PrecioU)
    if PrecioU>0:
        Precios.append(PrecioU)
    for x in range(1): 
       if PrecioU<0:
            print("El precio no es un valor positivo, por favor ingresar un valor correcto")
            PrecioU=input("Ingrese el precio unitario ")
            PrecioU=float(PrecioU)
    
    Pdesc=input("Ingrese el porcentaje de descuento ")
    Pdesc=float(Pdesc)
    for x in range(1):  
        if 0<=Pdesc<=100:
            PorcentajeDes.append(Pdesc)
    while 0>=Pdesc>=100:
            print("El valor de descuento es incorrecto, por favor ingresar un valor correcto")
    
print(Productos)
print(Precios)
print(PorcentajeDes)





