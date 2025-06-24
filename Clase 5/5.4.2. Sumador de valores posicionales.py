'''
Clase:        Clase 5
Tema:         Loops
Ejercicio:    5.4.2. Sumador de valores posicionales
Descripción:  Pide un número al usuario y suma sus dígitos hasta que quede un solo dígito. 

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''
a = list(map(int, input("Ingrese un número: ")))
b = sum(a)

print("Proceso de reducción para {}:".format(''.join(map(str, a))))
print("{} = {}".format(''.join(map(str, a)), b))
while b >= 10:
    b_ = str(b)
    b = (sum(map(int, str(b))))
    print("{} = {}".format(b_, b))
print(f"El resultado final es : {b}")
