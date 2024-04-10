# Crear un programa que permita jugar al clásico juego piedra, papel o tijeras. 
# El mismo debe pedir al usuario que ingrese su jugada, y utilizando la librería
#  random generar una elección para la máquina. Luego debe mostrar el ganador y 
#  preguntar al usuario si desea volver a jugar.
import random

while True:
    juego=["piedra","papel","tijera"]
    consola=random.choice(juego)
    jugador=input("Ingrese piedra , papel o tijera: ").lower()
    while True:
        if (jugador in juego):
            break
        else: 
            print("Lo que ingreso no es valido")
            jugador=input("Ingrese un valor valido: ").lower()
    while True:
        print("La consola saco: ",consola)
        if jugador=="piedra" and consola=="tijera":
            print("Felicidades ganaste")
            break
        elif jugador=="piedra" and consola=="papel":
            print("Has perdido")
            break
        elif jugador==consola:
            print("Empataron")
            break
        elif consola=="piedra" and jugador=="papel":
            print("Felicidades ganaste")
            break
        else: 
            print("Has perdido")
            break
    seguir=input("Desea volver a jugar? S/N: ").upper()
    while True:
        if seguir=="S" or seguir=="N":
            break
        else:
            seguir=input("Error ingrese S o N: ").upper()
    if seguir=="N":
        print("Gracias por jugar")
        break
    else:print("---------------------------")