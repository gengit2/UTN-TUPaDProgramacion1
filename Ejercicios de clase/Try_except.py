def crear_mochila():
    capacidad = int(input("Ingrese la capacidad para la mochila "))
    while True:
        try:
            if capacidad <= 0:
                raise ValueError
            
            return ["--Vacio--"] * capacidad
        except ValueError:
            print("Debe ingresas un numero mayor o igual a 0")
        except TypeError:
            print("Debe ingresas un número ")
            

def Mostrar_menu():
    print(" \n Menú de la mochila")
    print("1. Guardar un objeto")
    print("2. Ver contenido de la mochila")
    print("3. Salir")
    print("4. Eliminar un objeto de la mochila ")

def guardar_objeto(mochila):
    try: 
        pos = int(input(f"Ingrese la posición (0-{len(mochila)-1}): "))
        objeto = input("Ingrese el objeto que desea guardar en la mochila: ").strip()
        if objeto == "":
            print("No se puede dejar el objeto vacío")
            return 
        mochila[pos]= objeto
        print(f"El objeto '{objeto}' ha sido guardado en la posición {pos}.")

    except ValueError:
        print("Debe ingresar un número entero válido para la posición.")
    except IndexError:
        print(f"La posición debe estar entre 0 y {len(mochila)-1}.")

def ver_contenido(mochila):
    print("\n Contenido de la mochila ")
    for i, objeto in enumerate(mochila):
        print(f"Posicion {i}: {objeto}")

def eliminar_objeto(mochila):
    try:
        pos = int(input(f"Ingrese la posición (0-{len(mochila)-1}): "))
        if mochila[pos] == "--Vacio--":
            print("Esa posición ya está vacía. ")
        else:
            print(f"\n Eliminando el objeto de la posición {pos}")
            mochila[pos] = "--Vacio--"
    except ValueError: 
        print("Deber ingresar un número entero para la posición.")
    except IndexError:
        print(f"La posición debe estar entre o y {len(mochila)-1}")
        

mochila=crear_mochila()
while True:
    Mostrar_menu()
    opcion = input("Seleccione una opcion (1-4): ").strip()

    if opcion == "1":
        guardar_objeto(mochila)
    elif opcion == "2":
        ver_contenido(mochila)
    elif opcion == "3":
        print("Saliendo... ")
        break
    elif opcion == "4":
        eliminar_objeto(mochila)
    else:
        print("Opción inválida ")



