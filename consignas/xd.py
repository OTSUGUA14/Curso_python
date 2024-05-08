if opcion == '1':
        producto = input('Ingrese el nombre del producto: ')
        precio = int(input('Ingrese el precio del producto: $'))
        if producto in carrito :
            carrito[producto] += precio
        else:
            carrito[producto] = precio
            print(f'{producto} agregado al carrito.')
carrito = {}
while True:
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver carrito")
    print("4. Salir")
    opcion = input('\n Seleccione una opcion del menu:')
    if opcion == '1':
        producto = input('Ingrese el nombre del producto: ')
        precio = int(input('Ingrese el precio del producto: $'))
        if producto in carrito :
            carrito[producto] += precio
        else:
            carrito[producto] = precio
            print(f'{producto} agregado al carrito.')
    elif opcion == '2':
        producto = input('Ingrese el nombre del producto a eliminar: ')
        if producto in carrito:
            del carrito[producto]
            print(f'{producto} eliminado del carrito.')
        else:
            print(f'{producto} no esta en el carrito.')
    elif opcion == '3':
        total = 0
        if not carrito:
            print('El carrito esta vacio.')
        else:
            print('Carrito de compras: ')
            for producto, precio in carrito.items():
                print(f'{producto}: ${precio}')
                total += precio
                print(f'Total: ${total}')
    elif opcion == '4':
        print('Gracias por visitar el supermercado Totete.')
        break
    else:
        print('OPCION NO VALIDA. POR FAVOR INTENTE NUEVAMENTE.')