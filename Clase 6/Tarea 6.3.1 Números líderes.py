'''
Clase:        Clase 6
Tema:         Manejo de listas
Ejercicio:    6.3.1. Números líderes
Descripción:  Un número en una lista es "líder" si es estrictamente mayor que todos lkos elementos a su derecha. Dada una lista de 
números ingresada por el usuario, imprime todos los números líderes.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''

a = list(map(int, input("Ingrese un número: ").split(" ")))
# si el numero de la posicion x es mayor que todos de la derecha entonces es lider, si no 
# supongo que los lideres se guardan en una lista aparte de la metida 

lista = []
for i in range(len(a)):
    if i == len(a) - 1 or a[i] > max(a[i+1:]):
        lista.append(a[i])
if lista:
    lista.pop()
print(" ".join(map(str, lista)))
