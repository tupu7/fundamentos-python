#Dada una lista circular, determina cuántas
# rotaciones mínimas a la izquierda se
# necesitan para que esté en orden
# estrictamente ascendente. Si no es posible,
# imprime -1

#Osea que yo doy una lista y el numero menor, digamos 1, tiene a la izquierda numeros más grandes y el codigo tiene que ver cuantas veces mueve los numeros de la izquierda para 
# #que vayan en orden ascendente de izquierda a derecha.
# a = list(map( int, input("Escriba los numeros: ").split(" ")))
# cont = 0
# rupt = 0




# for i in range(len(a)-1) :
#     if a[i] >  a[i + 1]:
#         cont += 1
#         rupt = (i + 1) 

# if cont == 0:q
#     print(0)
# elif cont == 1:
#     print(rupt)
# else:
#     print(-1)


'''
Dado un arreglo de enteros, encuentra un
índice i tal que la suma de los elementos
desde el inicio hasta i sea igual a la suma
desde i+1 hasta el final. Si no existe, imprime
-1.
'''

a = list(map( int, input("Escriba los numeros: ").split(" ")))
suma_total = sum(a)
suma_izquierda = 0

for i in range(len(a)):
    suma_derecha = suma_total - suma_izquierda - a[i]
    if suma_izquierda == suma_derecha:
        print(i)
        break
    suma_izquierda += a[i]
else:
    print(-1)

# cont = 0
# suma = -1

# for i in range(len(a)):
#     if sum(a[i:]) == sum(a[:i]):
#         cont += i
#         suma = (i +1)
# print(suma)