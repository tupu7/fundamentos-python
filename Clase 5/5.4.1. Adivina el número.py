'''
Clase:        Clase 5
Tema:         Loops
Ejercicio:    5.4.1. ¡Adivina el número!
Descripción:  Genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine.
El programa debe seguir pidiendo números hasta que acierte. En cada
intento fallido el programa notificará al usuario si el número secreto es
mayor o menor al último valor ingresado.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
import random

a = random.randint(1, 100)

while True:
    b = int(input("Ingresa un numero entre 1 y 100: "))

    if b < a:
        print("El numero secreto es mayor")
    elif b > a:
        print("El numero secreto es menor")
    else:
        print(f"¡Felicidades has acertado el número secreto: {b}", "\n Fin del juego")
        