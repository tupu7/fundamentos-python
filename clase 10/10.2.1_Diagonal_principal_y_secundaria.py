'''
Clase:        Clase 10
Tema:         Matrices
Ejercicio:    10.2.1. Diagonal principal y secundaria
Descripción:  Dada una matriz cuadrada ingresada por el
usuario, crea dos listas, una con los
elementos de la diagonal principal y la otra
con los elementos de la diagonal
secundaria.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-06-10
Estado:       [ Terminado ]
'''

a = int(input())

lista = []
lista_principal = []
lista_secundaria = []

for i in range(a):
    rew = input()
    temp_list = list(map(int, rew.split(",")))
    lista.append(temp_list)
print(lista)

for i in range(len(lista)):
    for j in range(len(lista[i])):
        if i == j:
            lista_principal.append(lista[i][j])

        if i + j == len(lista )-1:
            lista_secundaria.append(lista[i][j])


print(lista_principal)
print(lista_secundaria)