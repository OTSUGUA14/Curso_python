# Creación de hilos con la librería threading
# Esta librería nos permite crear hilos de ejecución
# Los mismos se ejecutan de forma concurrente y son independientes entre sí
# Cada hilo tiene su propio flujo de ejecución
# Esto nos permite realizar tareas en paralelo y mejorar el rendimiento de nuestro programa

import threading    # Para trabajar con hilos utilizamos la librería threading

import time    # Para poder utilizar la función sleep, la cual detiene el programa X segundos 

def segundo_plano(flag_global):
    contador = 0
    while not flag_global.is_set():    # Mientras flag_global sea False
        contador += 1
        time.sleep(1)   # Detenemos el programa 1 segundos
    print("\nEl hilo se detuvo")
    print("Contador: ", contador,"\n") 
    
# Hemos definido una función llamada segundo_plano, la cual se ejecutará en segundo plano
# a través de un hilo de ejecución

# Para crear un hilo de ejecución utilizamos la función Thread de la librería threading
# Además, debemos crear una variable global que nos permita detener el hilo de ejecución
# Para ello, threading nos proporciona la función Event
# Esta función crea un objeto que nos permite controlar el hilo de ejecución

flag_global = threading.Event()     # flag que puede tomar el valor True o False de forma global
                                    # por defecto es False

# Creamos un menú sencillo con opciones para iniciar y detener el hilo de ejecución

while True:
    print("\n1. Iniciar hilo")
    print("2. Detener hilo")
    print("3. Salir")
    opcion = input("Opción: ")
    if opcion == "1":
        flag_global.clear()     # Nos aseguramos que flag_global sea False
        hilo = threading.Thread(target=segundo_plano, args=(flag_global, ))
        # El primer parámetro de la función Thread es la función que se ejecutará en segundo plano
        # El segundo parámetro es una tupla con los argumentos que recibe la función
        hilo.start()    # Iniciamos el hilo de ejecución
        print("\nHilo iniciado")
        
    elif opcion == "2":
        flag_global.set()   # Cambiamos el valor de flag_global a True
                            # Esto detiene el hilo de ejecución
        hilo.join()   # La función join espera a que el hilo de ejecución termine
        
    elif opcion == "3":
        if hilo.is_alive():     # Si el hilo de ejecución está activo
            flag_global.set()
            hilo.join()
        break

    else:
        print("\nOpción incorrecta")