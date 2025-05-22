'''
Clase:        Fase de fortalecimiento lógico
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.3.1. Automatizando el cálculo de la propina
Descripción:  Pide al usuario el total de una cuenta y el porcentaje de propina
(por ejemplo, 10%, 15%, 20%). Calcula y muestra en pantalla el total
a pagar.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''
a = int(input("Total de la cuenta: "))
b = int(input("Propina: "))
c = (f"Total de la cuenta con propina {b/a * 100}%: {a + b}$" )
print((c))

'''
Clase:        Fase de fortalecimiento lógico
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.3.2. Generador del correo de Key
Descripción:  Solicita al usuario su nombre completo (asume dos nombres y
dos apellidos). Luego, el programa generará, su correo con el
formato:
• primer_nombre.primer_apellido@keyinstitute.edu.sv

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

a = (input("Escriba su primer nombre: "))
b = (input("Escriba su segundo nombre: "))
c = (input("Escriba su primer apellido: "))
d = (input("Escriba su segundo apellido: "))
print(f"El correo que se debe asignar al usuario ingresado es:\n{a + '.' + c + '@keyinstitute.edu.sv'}")

'''
Clase:        Fase de fortalecimiento lógico
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.4.1. División con Precisión
Descripción:  Dados tres enteros a, b y k, imprime el resultado de a / b con k decimales exactos (sin
redondear)

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

a = int(input("Primer numero: "))
b = int(input("Segundo numero: "))
k = int(input("Decimales: "))

numero = a/b
numero = str(numero).split(".")
deci = len(numero[1])
entero = len(numero[0])

if deci == k:
    print(numero[0] + "." +  numero[1])
elif deci < k:
    falta = k - deci
    print(numero[0] + "." + 0*falta)
else:
    print(numero[0] + "." + numero[1][:k])

'''
Clase:        Fase de fortalecimiento lógico
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.4.2. Suma de cadenas de texto
Descripción:  Dados dos números enteros positivos muy grandes como cadenas de texto A y B.
Calcula (A + B) e imprímelo como cadena de texto.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ En progreso ]
'''


a = "12345678901234567890"
b = "98765432109876543210"

'''
Clase:        Fase de fortalecimiento lógico
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.4.3. Suma de fracciones
Descripción:  Dado un arreglo de n fracciones (representadas como cadenas "a/b"), calcula la suma
total y expresa el resultado como una fracción irreducible.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ En progreso ]
'''
n = int(input("Fracciones: "))
if n > 0:
    x = int(input("Numerador: "))
    y = int(input("denominador: ")) 
    print(x / y)
    x = str(x)
    y = str(y)
    print(x + "/" + y)
'''
Clase:        Fase de fortalecimiento lógico
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.4.2. Suma de cadenas de texto
Descripción:  Dados dos números enteros positivos muy grandes como cadenas de texto A y B.
Calcula (A + B) e imprímelo como cadena de texto.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ En progreso ]
'''

#Suma de cadenas

# a = "12345678901234567890"
# b = "98765432109876543210"

'''
Clase:        Fase de fortalecimiento lógico
Tema:         Variables, tipos, entradas y salidas
Ejercicio:    1.4.3. Suma de fracciones
Descripción:  Dado un arreglo de n fracciones (representadas como cadenas "a/b"), calcula la suma
total y expresa el resultado como una fracción irreducible.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ En progreso ]
'''
# n = int(input("Fracciones: "))
# if n > 0:
#     x = int(input("Numerador: "))
#     y = int(input("denominador: ")) 
#     print(x / y)
#     x = str(x)
#     y = str(y)
#     print(x + "/" + y)

'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloque condicional
Ejercicio:    2.3.1. Contraseña segura
Descripción:  Solicita una cadena de texto que representa una contraseña, y verifica si la contraseña
cumple con las siguientes condiciones: tener al menos 8 caracteres, un número y una
mayúscula.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

a = input("Coloca la contraseña: ")


mayus = False
digito = False

if len(a) >= 8:
    for caracter in a:
        if caracter.isupper():
            mayus = True
        if caracter.isdigit():
            digito = True
    if mayus and digito:
        print("Contraseña segura")
    else:
        print("Constraseña no segura")



'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloque condicional
Ejercicio:    2.3.2. Cálculo de impuesto
Descripción:  Desarrollar un programa en Python que permita calcular el impuesto que debe pagar
un usuario por el consumo de energía. El cálculo debe realizarse basado en la siguiente
tabla.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

a = (int(input("Ponga el valor de las unidades: ")))

if 0 <= a <= 100:
    print("0")

elif 101  <= a <= 200:
    print((a * 0.5))

elif a >= 201:
    print(a * 0.7)



'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloque condicional
Ejercicio:    2.4.1. El número mágico
Descripción:  Crea un programa en Python para determinar si un número es "mágico“.
Un número es “mágico” si es divisible por 7 pero no por 5.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

a = 35

magico = False
normal = False

if a % 7 == 0 and a % 5 != 0: 
    magico = True
else:
    normal = True

if magico and not normal:
    print("magico")
else:
    print("normal")


'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloque condicional
Ejercicio:    2.4.2. Año bisiesto
Descripción:  Determina si un año es bisiesto, considerando las reglas gregorianas. Para que un año
sea bisiesto, debe cumplir alguna de las siguientes condiciones:
• Si es divisible por 4.
• Si es divisible por 100 y por 400.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

a = 1900

if a % 4 ==0 or (a % 100 == 0 and a % 400 == 0):
    print("año bi")
else:
    print("Año normal")

'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloque condicional
Ejercicio:    2.5.1. Elevador lógico
Descripción:  En un edificio hay dos elevadores (A y B) en distintos pisos. Un usuario llama al elevador
desde un piso p. El elevador más cercano responde, pero si ambos están a la misma
distancia, elige el A.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''

import math

a = 10
b = 7

p = 9

elevaddor_A = math.fabs(a-p)
elevaddor_B = math.fabs(b-p)

if elevaddor_A < elevaddor_B:
    print("Elevador A")
elif elevaddor_A > elevaddor_B:
    print("Elevador B")
else:
    print("Elevador A")

'''
Clase:        Fase de fortalecimiento lógico
Tema:         Bloque condicional
Ejercicio:    2.5.2. Punto en zona de peligro
Descripción: Eres parte del equipo de desarrollo de un sistema de defensa automatizado para una
base científica ubicada en una zona volcánica peligrosa. Por cuestiones de seguridad, el
sistema debe identificar si un objeto detectado por sensores (un punto con
coordenadas (x, y)) se encuentra en una zona peligrosa, de manera que pueda activarse
una alerta inmediata. Las zonas de peligro están definidas como:
• Zona de peligro 1: el punto se encuentra en el primer cuadrante, es decir, x > 0 y y > 0.
• Zona de peligro 2: el punto está dentro de un círculo de radio 5 centrado en el origen
(0, 0), es decir, x² + y² <= 25.

Autor:        Eduardo Noé Figueroa Rodríguez
Fecha:        2025-05-15
Estado:       [ Terminado ]
'''


x = 5
y = -10

if x**2 + y**2 <= 25:
    print("Peligro")
else:
    print("Seguro")