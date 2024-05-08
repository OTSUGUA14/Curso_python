# Sistema de Gestión de Inventarios:
#  Desarrolla un programa que permita a un usuario gestionar un inventario de productos. 
# Debe incluir funciones para agregar nuevos productos, 
# actualizar información de productos existentes, eliminar productos, 
# mostrar el inventario completo y
# buscar productos por diferentes criterios (nombre, categoría, precio, etc.).

def agregar(productos):
    
    while True:
        producto=input("Ingrese el nombre del producto: ")
        categoria=input("Ingrese la categoria del producto: ")
        precio=int(input("Ingrese el precio: "))
        cantidad=int(input("Ingrese la cantidad: "))
        ingreso={}
        ingreso.update({"elemento":producto,"categoria":categoria, "precio": precio, "cantidad":cantidad})
        productos.append(ingreso)
        pregunta=input("desea agregar otro producto? S/N ")
        print("--------------------------------------")
        pregunta=pregunta.lower()
        if pregunta=="n":
            break
            
def modificar(productos):
    
    while True:
        aux=0
        print("--------------------------------------")
        for i in productos:
            aux+=1
            print(aux, i)   
        print("--------------------------------------")
        modi=input("Ingrese el elemento que quiere modificar segun su nombre:").lower()

        se_encontro=0
        for i in range(len(productos)):
            if modi == productos[i]["elemento"]:
                se_encontro=1
                while True:
                    cambiar=input("Ingrese el dato del producto que quiere cambiar nombre ,categoria, precio, cantidad  :").lower()
                    if cambiar=="nombre":
                        cambio=input("Ingrese el nuevo nombre del producto: ")
                        productos[i]["elemento"]=cambio
                        break
                    elif cambiar=="categoria":
                        cambio=input("Ingrese la nueva categoria del producto: ")
                        productos[i]["categoria"]=cambio
                        break
                    elif cambiar=="cantidad":
                        cambio=input("la nueva cantidad de producto: ")
                        productos[i]["cantidad"]=cambio
                        break
                    elif cambiar=="precio":
                        cambio=input("Ingrese el nuevo precio del producto: ")
                        productos[i]["precio"]=cambio
                        break
                    else:
                        print("Error ingrese un valor valido")
        if se_encontro==0:
            print("No se encontro el elemento, ingrese un nombre valido: ")
        else:
            pregunta=input("desea modificar otro producto? S/N ").lower
            if pregunta=="n":
                break
            break

def eliminar(productos):
    se_encontro=0
    while True:
        aux=0
        print("--------------------------------------")
        for i in productos:
            aux+=1
            print(aux, i)   
        print("--------------------------------------")
        eli=input("Ingrese el elemento que quiere eliminar segun su nombre:").lower()
        se_encontro=0
        for nombre in productos:
            if nombre.get("elemento") == eli:
                productos.remove(nombre)
                se_encontro=+1
                print("Elmento eliminado")
            break
        if se_encontro==0:
            print("No se encontro el elemento, ingrese un nombre valido: ")
        else:
            pregunta=input("desea eliminar otro producto? S/N ").lower
            if pregunta=="n":
                break
            print("--------------------------------------")
            break

def buscar_elemento(productos):
    se_encontro=False
    buscar=input("Si decea buscar por criterio de nombre o categoria ingrese S , de lo contrario ingrese otra tecla: ").lower()
    if buscar=="s":
        st=input("ingrese el nombre o categoria de de quiere encontrar: ")
        for elemento in productos:
            if elemento.get("elemento") == st:
                if se_encontro:
                    print(elemento)
                else:
                    se_encontro=True
                    print("Elemento encontrado:")
                    print(elemento)
                
            if elemento.get("categoria") == st:
                if se_encontro:
                    print(elemento)
                else:
                    se_encontro=True
                    print("Elemento encontrado:")
                    print(elemento)
    else:
        numero=int(input("ingrese la cantidad de  precio o cantidad de de quiere encontrar: "))
        for elemento in productos:
            
            if elemento.get("cantidad") == numero:
                if se_encontro:
                    print(elemento)
                else:
                    se_encontro=True
                    print("Elemento encontrado:")
                    print(elemento)
                
            if elemento.get("precio") == numero:
                if se_encontro:
                    print(elemento)
                else:
                    se_encontro=True
                    print("Elemento encontrado:")
                    print(elemento)
                
           
                
    if not se_encontro:
        print("No se encontro ningun producto")
productos=[]



while True:
    print(" ")
    print("--------------------------------------")
    print("1: Agregar elemento")
    print("2: Modificar elemento")
    print("3: Eliminar elementos")
    print("4: Mostras elementos")
    print("5: Buscar elementos")
    print("6: Salir")
    print("--------------------------------------")
    print(" ")
    opcion=int(input("Elige la opcion que desea: "))
    if opcion==1:
        agregar(productos)
    elif opcion==2:
        modificar(productos)
    elif opcion==3:
        eliminar(productos)
    elif opcion==4:
        for i in productos:
            
            print(i)    
    elif opcion==5:
        buscar_elemento(productos)
    elif opcion==6:
        pass