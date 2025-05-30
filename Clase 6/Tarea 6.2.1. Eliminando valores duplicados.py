'''
Clase:        Clase 6
Tema:         Manejo de listas
Ejercicio:    6.2.1. Eliminando valores duplicados 
Descripción:  Dada una lista ingresada por el usuario, elimina los elementos duplicados manteniendo la primera aparición de cada número
Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-30
Estado:       [ Terminado ]
'''


a = list(map ( int, input("lista de numeros: ").split()))


lista_sin_duplicados = []

for i in a:
    if i not in lista_sin_duplicados:
        lista_sin_duplicados.append(i)

print(lista_sin_duplicados)
    