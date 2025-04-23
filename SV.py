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
    while PrecioU<0: 
        print("El precio no es un valor positivo, por favor ingresar un valor correcto")
        PrecioU=input("Ingrese el precio unitario ")
        PrecioU=float(PrecioU)
    else:
         Precios.append(PrecioU)
        
    
    Pdesc=input("Ingrese el porcentaje de descuento ")
    Pdesc=float(Pdesc)
    if 0<=Pdesc<=100:
            PorcentajeDes.append(Pdesc)      
    while Pdesc<0 or Pdesc>100:
        print("El valor de descuento es incorrecto, por favor ingresar un valor correcto")
        Pdesc=input("Ingrese el porcentaje de descuento ")
        Pdesc=float(Pdesc)
    else:
         PorcentajeDes.append(Pdesc)
    

print(Productos)
print(Precios)
print(PorcentajeDes)
