import json
with open("ejemplo.json", "r") as file:
    data = json.load(file)

# 1
def agregar_estudiante(data):
    nombre = input("Ingrese el nombre del estudiante: ")
    materias = {
        "Matematicas": [],
        "Fisica": [],
        "Progra": [],
        "IntroInge": [],
        "DP": []
    }
    estudiante = {"nombre": nombre, "materias": materias}
    data["estudiantes"].append(estudiante)
    with open("ejemplo.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Estudiante agregado:", nombre)

# 2
def ver_estudiantes(data):
    for i, estudiante in enumerate(data["estudiantes"], start=1):
        print(f"{i}. {estudiante['nombre']}")

# 3
def actualizar_nota(data, estudiante, materia, nueva_nota):
    for alumno in data["estudiantes"]:
        if alumno["nombre"] == estudiante: 
            if materia in alumno["materias"]:
                alumno["materias"][materia].append(nueva_nota) 
                print(f"Nota actualizada: {materia} ahora tiene la nota {nueva_nota} añadida.")
                return True  
            else:
                print(f"La materia '{materia}' no existe para este estudiante.")
                return False  
    print(f"No se encontró al estudiante '{estudiante}'.")
    return False 
def agregar_notas(data):
    materias_opciones = ["Matematicas", "Fisica", "Progra", "IntroInge", "DP"]
    estudiante = input("Ingrese el nombre del estudiante al que desea agregar una nota: ")
    estudiante_obj = None
    for alumno in data["estudiantes"]:
        if alumno["nombre"] == estudiante:
            estudiante_obj = alumno
            return

    if not estudiante_obj:
        print(f"No se encontró al estudiante '{estudiante}'.")
        return
    print("Seleccione la materia:")
    for i in range(len(materias_opciones)):
        print(f"{i + 1}. {materias_opciones[i]}")
    try:
        materia_seleccionada = int(input("Ingrese el número de la materia: "))
        if materia_seleccionada < 1 or materia_seleccionada > len(materias_opciones):
            print("Opción de materia no válida.")
            return
        materia = materias_opciones[materia_seleccionada - 1]
    except ValueError:
        print("Error: Debe ingresar un número.")
        return
    try:
        nueva_nota = float(input("Ingrese la nueva nota (número): "))
    except ValueError:
        print("Error: La nota debe ser un número.")
        return
    if materia in estudiante_obj["materias"]:
        estudiante_obj["materias"][materia].append(nueva_nota)
        print(f"Nota actualizada: {materia} ahora tiene la nota {nueva_nota} añadida.")
        with open("ejemplo.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print(f"La materia '{materia}' no existe para este estudiante.")

# 4
def calcular_promedios(data):
    promedios_estudiantes = []  
    for estudiante in data["estudiantes"]:
        nombre = estudiante["nombre"]
        materias = estudiante["materias"]

        suma_total = 0
        cantidad_total = 0
        promedios_materias = [] 

        for materia in materias: 
            calificaciones = materias[materia] 
            if calificaciones: 
                promedio_materia = sum(calificaciones) / len(calificaciones)
            else:
                promedio_materia = 0  

            promedios_materias.append((materia, promedio_materia))  
            suma_total += sum(calificaciones)
            cantidad_total += len(calificaciones)

        promedio_general = suma_total / cantidad_total if cantidad_total > 0 else 0

        promedios_estudiantes.append({
            "nombre": nombre,
            "promedios_materias": promedios_materias,
            "promedio_general": promedio_general
        })  
#5
    return promedios_estudiantes
def mostrar_promedios(data):
    print("Lista de estudiantes:")
    for estudiante in data["estudiantes"]:
        print(f"- {estudiante['nombre']}")
    nombre_estudiante = input("Ingrese el nombre del estudiante para calcular los promedios: ")
    for estudiante in data["estudiantes"]:
        if estudiante["nombre"] == nombre_estudiante:
            materias = estudiante["materias"]
            suma_total = 0
            cantidad_total = 0
            promedios_materias = []

            for materia in materias:
                calificaciones = materias[materia]
                if calificaciones:
                    promedio_materia = sum(calificaciones) / len(calificaciones)
                else:
                    promedio_materia = 0

                promedios_materias.append((materia, promedio_materia))
                suma_total += sum(calificaciones)
                cantidad_total += len(calificaciones)

            promedio_general = suma_total / cantidad_total if cantidad_total > 0 else 0
            print(f"\nEstudiante: {nombre_estudiante}")
            print("Promedios por materia:")
            for materia, promedio in promedios_materias:
                print(f"  {materia}: {promedio:.2f}")
            print(f"Promedio general: {promedio_general:.2f}\n")
            return
    print(f"No se encontró al estudiante '{nombre_estudiante}'.")
#6
def mejor_promedio_por_materia(data):
    materia_solicitada = input("Ingrese el nombre de la materia para buscar el mejor promedio: ")
    mejor_promedio = 0
    mejor_estudiante = None
   
    for estudiante in data["estudiantes"]:
        materias = estudiante["materias"]
       
        if materia_solicitada in materias:
            calificaciones = materias[materia_solicitada]
            if calificaciones:  # Si hay calificaciones
                promedio = sum(calificaciones) / len(calificaciones)
            else:
                promedio = 0
            if promedio > mejor_promedio:
                mejor_promedio = promedio
                mejor_estudiante = estudiante["nombre"]

    if mejor_estudiante:
        print(f"\nEl mejor promedio en {materia_solicitada} es de {mejor_estudiante} con un promedio de {mejor_promedio:.2f}.")
#7
def mejor_estudiante(data):
    mejor_promedio = 0
    mejor_estudiante = None
    for estudiante in data["estudiantes"]:
        nombre = estudiante["nombre"]
        materias = estudiante["materias"]

        suma_total = 0
        cantidad_total = 0

        for materia, calificaciones in materias.items():
            suma_total += sum(calificaciones)
            cantidad_total += len(calificaciones)

        promedio_general = suma_total / cantidad_total if cantidad_total > 0 else 0


        if promedio_general > mejor_promedio:
            mejor_promedio = promedio_general
            mejor_estudiante = nombre

    if mejor_estudiante:
        print(f"\nEl mejor estudiante es {mejor_estudiante} con un promedio general de {mejor_promedio:.2f}.")

while True:
    print("\n")
    n = input(
        "Ingrese el número de la opción que desea realizar:\n"
        "1. Agregar estudiante al diccionario\n"
        "2. Ver todos los estudiantes\n"
        "3. Agregar notas\n"
        "4. Calcular promedios\n"
        "5. Mejor promedio por materia\n"
        "6. Mejor estudiante\n"
        "7. Salir\n"
    )

    if n == '1':
        agregar_estudiante(data)
    elif n == '2':
        ver_estudiantes(data)
    elif n == '3':
        agregar_notas(data)
    elif n == '4':
        mostrar_promedios(data)
    elif n == '5':
        mejor_promedio_por_materia(data)
    elif n == '6':
        mejor_estudiante(data)
    elif n == '7':
        print("Terminamos por hoy")
        break
    else:
        print("Opción no válida. Intente de nuevo.")