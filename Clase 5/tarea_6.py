# import random

# a = random.randint(1, 100)

# while True:
#     b = int(input("Ingresa un numero entre 1 y 100: "))

#     if b < a:
#         print("El numero secreto es mayor")
#     elif b > a:
#         print("El numero secreto es menor")
#     else:
#         print(f"¡Felicidades has acertado el número secreto: {b}", "\n Fin del juego")
#         break

'''
El usuario ingresa un numero
Ese numero si tiene más de un digito va a ir sumando los digitos uno por uno
Si el resultado de la suma de los digitos es mayor que uno ese resultado se va a seguir sumando
Asi sucesivamente hasta que el resulato tenga solo un digito
'''
a = int(input("Ingresa un numero: "))

while a >= 10:
    print("hola")