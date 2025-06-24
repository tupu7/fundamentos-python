import json
with open("categorias_prueba.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def ver_noticias(data):
        print("Opciones:")
        print("1. Ver noticias de la categoría Deportes")
        print("2. Ver el menú de los almuerzos del día")
        print("3. Ver actividades adicionales")
        print("4. Ver Actividades obligatorias")
        print("5. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            deportes = data["Noticias"]["Deportes"]
            print("Noticias de la categoría Deportes:")
            for i, deporte in enumerate(deportes):
                nombre = deporte.get("Nombre", "")
                print(f"{i}. {nombre}")
            a = (input("Seleccione el deporte que desea ver: ")).strip().lower()
            for deporte in deportes:
                enocontrar = False
                if a == deporte["Nombre"].strip().lower():
                    print(f"Nombre: {deporte["Nombre"]}")
                    print(f"Salidas: {deporte["Salidas"]}")
                    print("Torneos:")
                    for i,torne in deporte["Torneos"].items():
                        print(f"{i}: {torne}")
                    enocontrar = True
                    break
            else:
                print("No se encontró el deporte seleccionado.")   

        elif opcion == 2:
            if "Menú de los almuerzos del día" in data["Noticias"]:
                noticias = data["Noticias"]["Menú de los almuerzos del día"]
                print("Menú de los almuerzos del día:")
                for menu in noticias:
                    for dia, plato in menu.items():
                        print(f"{dia}: {plato}")
            else:
                print("No hay noticias del menú disponibles.")


        elif opcion == 3:
            noticias = data["Noticias"]["Actividades adicionales"]
            for actividad in noticias:
                for actividad, descripcion in actividad.items():
                    print(f"{actividad}: {descripcion}")
            else:
                print("No hay actividades adicionales disponibles.")

        elif opcion == 4:
            actividades = data["Noticias"]["Actividades obligatorias"]
            eleccion = input("¿Qué actividad quiere ver? (KeyWeek/HorasKey): ").strip().lower()
            if eleccion in ["keyweek", "key", "keyw","KeyWeek"]:
                for nombre, info in actividades["KeyWeek"].items():
                    print(f"  {nombre}:")
                    print(f"    Descripción: {info['Descripción']}")
                    print(f"    Horario: {info['horario']}")
            elif eleccion in ["horaskey", "horas", "horakey", "horask", "HorasKey"]:
                for nombre, info in actividades["HorasKey"].items():
                    print(f"  {nombre}:")
                    print(f"    Descripción: {info['Descripción']}")
                    print(f"    Cuantas horas: {info['Cuantas horas']}")
            else:
                print("Opción no válida.")

        elif opcion == 5:
            print("Hasta la próxima")
        else:
            print("Opción no válida.")



def agregar_noticias(data):
    print("1. Deportes", "\n" "2. Menú de los almuerzos del día", "\n" "3. Actividades adicionales", "\n" "4. Actividades obligatorias", "\n" "5. Salir")
    a = int(input("¿Cuál deporte quiere modificar? (seleccione un número) "))

    if a == 1:
        nombre = input("Nombre del deporte: ")
        salida = input("Descrpicion de la salida: ")
        torneo = {}
        while True:
            nombre_torneo = input("Nombre del torneo: ")
            if not nombre_torneo:
                break
            descri_torneo = input("Descripción del torneo: ")
            
            torneo[nombre_torneo] = descri_torneo
            nuevo = {
                "Nombre": nombre,
                "Salidas": salida,
                "Torneos": torneo,
            }
    
        data["Noticias"]["Deportes"].append(nuevo)
        print("Deporte agregado.")

    if a == 2:
        menu = {}
        for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
            menu[dia] = input(f"Menú para {dia}: ")
        data["Noticias"]["Menú de los almuerzos del día"].append(menu)
        print("Almuerzo agregado")

    if a == 3:
        acti = {}
        while True:
            nombre_acti = input("Nombre: ")
            descri_acti = input("Descripción: ")
            if not nombre_acti:
                break
            acti[nombre_acti] = descri_acti

            nuevo = {
                "Nombre": nombre_acti,
                "Descripción": descri_acti
            }
            data["Noticias"]["Actividades adicionales"].append(nuevo)
            print("Actividad agregada.")

    if a == 4:
        acti_obi = input("KeyWeek u HorasKey: ").strip().lower()
        if acti_obi in ["keyweek", "key", "keyw"]:
            nombre = input("Nombre de la actividad KeyWeek: ")
            descripcion = input("Descripción: ")
            horario = input("Horario: ")

            data["Noticias"]["Actividades obligatorias"]["KeyWeek"][nombre] = {
                "Descripción": descripcion,
                "Horario": horario,
            }
            print("Actividad de la KeyWeek agregadada")

        elif acti_obi in ["horaskey", "horas", "horakey", "horask"]:
            nombre = input("Nombre de la actividad HorasKey: ")
            descripcion = input("Descripción: ")
            horas = input("Cuantas horas: ")
        
            data["Noticias"]["Actividades obligatorias"]["KeyWeek"][nombre] = {
                "Descripción": descripcion,
                "Horario": horario
            }
            print("Actividad de las HorasKey agregadada")

        else:
            nombre = input("Nombre de la actividad obligatoria: ")
            descripcion = input("Descripción: ")
            horas = input("Cuantas horas: ")

            data["Noticias"]["Actividades obligatorias"][nombre]= {
                "Descripción": descripcion,
                "Horas": horas
            }
            print("Actividad agregada")



    with open("categorias_prueba.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

while True:
    print("\n")
    n = input(
        "¿Qué desea hacer?\n"
        "1. Ver información\n"
        "2. Agregar noticia o actividad\n"
        "3. Salir\n"
        "Seleccione una opción: "
    )

    if n == "1":
        ver_noticias(data)
    elif n == "2":
        agregar_noticias(data)
    elif n == "3":
        print("Hasta la próxima")
        break
    else:
        print("Opción no válida.")