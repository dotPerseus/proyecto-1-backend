def cargar_tareas():
    tareas = []

    try:
        with open("tareas.txt", "r") as archivo:
            for linea in archivo:
                tareas.append(linea.strip())
    except FileNotFoundError:
        pass

    return tareas

def guardar_tarea(tarea):
    with open("tareas.txt", "a") as archivo:
        archivo.write(tarea + "\n")

def ver_tareas(tareas):
    if len(tareas) == 0:
            print("No hay tareas pendientes.")
    else:
        print("\nLista de tareas: ")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")
    
def agregar_tarea(tareas):
    nueva_tarea = input("Escribe la nueva tarea: ")
    if nueva_tarea.lower() in [t.lower() for t in tareas]:
        print ("Esa tarea ya existe.")
    else:
        tareas.append(nueva_tarea)
        guardar_tarea(nueva_tarea)
        print("Tarea agregada correctamente.")
    

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Salir")

tareas = cargar_tareas()

while True:
    mostrar_menu()
    opcion = input("Selecciona una opcion: ")

    if opcion == "1":
        ver_tareas(tareas)
        
    elif opcion == "2":
        agregar_tarea(tareas)
        
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("\n Opción inválida.")
