### Adivina el número (juego)

# Crear un programa en el que el usuario deberá adivinar el número que la máquina escogió. 
# Deben utilizar la librería `random` para generar la elección de la máquina. 
# El usuario tendrá 5 vidas, cada vez que intente adivinar, recibirá como respuesta 
# “El número es mayor” o “El número es menor” según corresponda, y perderá una vida.
# Ganará cuando logre adivinar el número elegido por la máquina.
import random 
numero=random.randint(1,50)
vidas=5
print(numero)
adivi=int(input("ingrese un numero entre el 1 y 50  tendras 5 vidas para advinar el número: "))
while vidas>1:
    if adivi>numero:
        print("--------------------------------")
        print("El numero es menor")
        vidas-=1
        print("Te quedan: " ,vidas," Vidas")
        adivi=int(input("Ingrese otro numero: "))
    elif  adivi<numero:
        print("--------------------------------")
        print("El numero es mayor")
        vidas-=1
        print("Te quedan: " ,vidas, " Vidas")
        adivi=int(input("Ingrese otro numero: "))
    else:
        print("--------------------------------")
        print("Felicidades adivinaste el numero ")
        break
if vidas==0:
    print("Mala suerte has perdido el número era: ", numero)