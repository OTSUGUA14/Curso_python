# Diseñar un programa que simule un carrito de compras, el mismo debe contar con un menú que contenga las siguientes opciones:

# 1. Agregar producto
# 2. Eliminar producto
# 3. Ver lista de compras
# 4. Finalizar compra
# 5. Salir

# Los productos disponibles son:

# Leche $50 - Galletas $35 - Gaseosa $87 - Huevos $66 - Aceite $110 - Pan $20

# Al finalizar la compra, debe “imprimirse” el ticket de compra, el cual contendrá la lista de productos y el precio final.
def agregar(comprar,productos,cantidad):
    print("Productos:")
    print("----------------------")
    longitud_maxima = max(len(producto) for producto in productos)
    contador=1
    for i in productos:
        
        print(contador,"", i.ljust(longitud_maxima), "precio: ", productos[i])
        contador+=1
    print("----------------------")
    agregar=int(input("Eliga el producto en base al numero de la posicion 1-6: "))
    while True:
        if agregar==1:
            cant=int(input("ingrese la cantidad de Leche que quiere llevar: "))
            
            if "Leche" in comprar:
                comprar["Leche"]=comprar["Leche"]+cant*50
                cantidad["Leche"]=cantidad["Leche"]+cant
                break
            else:
                comprar["Leche"]=50*cant
                cantidad["Leche"]=cant
                break
        elif agregar==2:
            cant=int(input("ingrese la cantidad de Galletas que quiere llevar: "))
            
            if "Galletas" in comprar:
                comprar["Galletas"]=comprar["Galletas"]+cant*35
                cantidad["Galletas"]=cantidad["Galletas"]+cant            
                break
            else:
                comprar["Galletas"]=35*cant
                cantidad["Galletas"]=cant
                break
        elif agregar==3:
            cant=int(input("ingrese la cantidad de Gaseosas que quiere llevar: "))
            
            if "Gaseosa" in comprar:
                comprar["Gaseosa"]=comprar["Gaseosa"]+cant*87
                cantidad["Gaseosa"]=cantidad["Gaseosa"]+cant
                break
            else:
                comprar["Gaseosa"]=87*cant
                cantidad["Gaseosa"]=cant
                break
        elif agregar==4:
            cant=int(input("ingrese la cantidad de Huevo que quiere llevar: "))
            
            if "Huevo" in comprar:
                cantidad["Huevo"]=cantidad["Huevo"]+cant
                comprar["Huevo"]=comprar["Huevo"]+cant*66
                break
            else:
                cantidad["Huevo"]=cant
                comprar["Huevo"]=66*cant
                break
        elif agregar==5:
            cant=int(input("ingrese la cantidad de Aceite que quiere llevar: "))

            if "Aceite" in comprar:
                cantidad["Aceite"]=cantidad["Aceite"]+cant
                comprar["Aceite"]=comprar["Aceite"]+cant*110
                break
            else:
                cantidad["Aceite"]=cant
                comprar["Aceite"]=110*cant
                break
        elif agregar==6:
            cant=int(input("ingrese la cantidad de Pan que quiere llevar: "))
            
            if "Pan" in comprar:
                cantidad["Pan"]=cantidad["Pan"]+cant
                comprar["Pan"]=comprar["Pan"]+cant*20
                break
            else:
                cantidad["Pan"]=cant
                comprar["Pan"]=20*cant
                break
        else:
            print("Error valor ingresao no valido")
            agregar=int(input("Ingrese un valor valido"))
    print("Producto agregado correctamente")
    
def eliminar(comprar,cantidad):
    longitud_maxima = max(len(producto) for producto in comprar)
    contador=1
    print("----------------------")
    print("Eliga el producto que desea eliminar")
    print("----------------------")
    
    for i in comprar:
        print(contador,"", i.ljust(longitud_maxima), " precio total: ", comprar[i], " cantidad:",cantidad[i])
       
        contador+=1
    print("----------------------")
    eliminar=input("Eliga el producto en base a su nombre ").lower()
    while True:
        if eliminar =="leche":
            comprar.pop("Leche")
            print("Producto eliminado correctamente")
            break
        elif eliminar =="galletas":
            comprar.pop("Galletas")
            print("Producto eliminado correctamente")
            break
        elif eliminar =="gaseosa":
            comprar.pop("Gaseosa")
            print("Producto eliminado correctamente")
            break
        elif eliminar =="huevos":
            comprar.pop("Huevos")
            print("Producto eliminado correctamente")
            break
        elif eliminar =="aceite":
            comprar.pop("Aceite")
            print("Producto eliminado correctamente")
            break
        elif eliminar =="pan":
            comprar.pop("Pan")
            print("Producto eliminado correctamente")
            break
        else :print("ERROR")
        eliminar=input("Ingrese un nombre valido: ")

def ver(comprar,cantidad):
    print("Lista de compra")
    print("----------------------")
    longitud_maxima = max(len(producto) for producto in comprar)
    contador=1
    for i in comprar:
        print(contador,"", i.ljust(longitud_maxima), " precio total: ", comprar[i], " cantidad:",cantidad[i])
       
        contador+=1
    print("----------------------")

def finalizar(comprar,cantidad):
    print("Lista Final")
    print("----------------------")
    longitud_maxima = max(len(producto) for producto in comprar)
    contador=1
    for i in comprar:
        print(contador,"", i.ljust(longitud_maxima), " precio total: ", comprar[i], " cantidad:",cantidad[i])
        contador+=1
    total=0
    for i in comprar:
        total+=comprar[i]
    print("Cantidad a pagar: ",total)
    print("----------------------")
productos={ "Leche":50, 
        "Galletas":35, 
        "Gaseosa":87, 
        "Huevos":66, 
        "Aceite":110, 
        "Pan" :20}
comprar={}
cantidad={"Leche":0, 
        "Galletas":0, 
        "Gaseosa":0, 
        "Huevos":0, 
        "Aceite":0, 
        "Pan" :0

}
while True:
    print("----------------------")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver lista de compras")
    print("4. Finalizar compra")
    print("5. Salir")
    print("----------------------")

    opcion=int(input("Eliga una opcion: "))
    if opcion==1:
        agregar(comprar,productos,cantidad)
        
    elif opcion==2:
        eliminar(comprar,cantidad)
    elif opcion==3:
        ver(comprar,cantidad)
    elif opcion==4:
        finalizar(comprar,cantidad)
    elif opcion==5:
        print("Gracias por su visita")
        break
    else:
        print("Eror ingrese un valor valido")
    
