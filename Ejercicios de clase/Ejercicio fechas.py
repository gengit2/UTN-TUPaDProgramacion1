dia_letra = str(input("Ingrese el día en letras "))
mes_actual= int(input("Ingrese el número del mes "))
dia_numero = int(input("Ingrese el número de día "))
cant_alumnos = None
cant_aprobados = None
cant_desaprobados = None
promedio_aprobados = None
promedio_desaprobados = None
cant_alumnosCiclo = None

asistencia = None
auxDia_letra=False
auxDia_numero=False
auxMes_actual=False

dia_letra= dia_letra.lower()

if (dia_letra == "lunes" or dia_letra == "martes" or dia_letra == "miercoles" or dia_letra == "jueves" or dia_letra =="viernes"):
    auxDia_letra = True
else:
    print("Ingrese un dia válido (Lunes,Martes,Miercoles,Jueves,Viernes)")

if (dia_numero >=1 and dia_numero <= 31 ):
    auxDia_numero= True
else:
    print("Ingrese un número de dia entre 1 y 31")

if (mes_actual >=1 and mes_actual <=12):
    auxMes_actual = True
else:
    print("Ingrese un número del mes entre 1 y 12")

if auxDia_letra == False or auxDia_numero == False or auxMes_actual == False:
    print("Error. El dia, número de día o número del mes es inválido")
elif(dia_letra == "lunes" or dia_letra == "martes" or dia_letra=="miercoles") and (dia_numero >=1 and dia_numero<=9) and (mes_actual>=1 and mes_actual<=9) :
    print(f"Fecha actual: {dia_letra} , 0{dia_numero} / 0{mes_actual}")
    examen_validar=input("¿Se tomaron exámenes? si/no ")
    examen_validar= examen_validar.lower()
    if examen_validar == "si":
        cant_aprobados = int(input("Ingrese la cantidad de aprobados "))
        cant_desaprobados = int(input("Ingrese la cantidad de desaprobados "))
        cant_alumnos = cant_aprobados + cant_desaprobados
        promedio_aprobados = cant_aprobados*100/cant_alumnos
        promedio_desaprobados = cant_desaprobados*100/cant_alumnos
        print(f"El promedio de alumnos desaprobados fue del {promedio_desaprobados}% y el promedio de alumnos aprobados fue del {promedio_aprobados}% ")
elif (dia_letra == "lunes" or dia_letra == "martes" or dia_letra=="miercoles") and (mes_actual>=1 and mes_actual<=9):
    print(f"Fecha actual: {dia_letra} , {dia_numero} / 0{mes_actual}") 
    examen_validar=input("¿Se tomaron exámenes? si/no ")
    examen_validar= examen_validar.lower()
    if examen_validar == "si":
        cant_aprobados = int(input("Ingrese la cantidad de aprobados "))
        cant_desaprobados = int(input("Ingrese la cantidad de desaprobados "))
        cant_alumnos = cant_aprobados + cant_desaprobados
        promedio_aprobados = cant_aprobados*100/cant_alumnos
        promedio_desaprobados = cant_desaprobados*100/cant_alumnos
        print(f"El promedio de alumnos desaprobados fue del {promedio_desaprobados}% y el promedio de alumnos aprobados fue del {promedio_aprobados}% ")
elif(dia_letra == "lunes" or dia_letra == "martes" or dia_letra=="miercoles") and (dia_numero>=1 and dia_numero<=9) :
    print(f"Fecha actual: {dia_letra} , 0{dia_numero} / {mes_actual}") 
    examen_validar=input("¿Se tomaron exámenes? si/no ")
    examen_validar= examen_validar.lower()
    if examen_validar == "si":
        cant_aprobados = int(input("Ingrese la cantidad de aprobados "))
        cant_desaprobados = int(input("Ingrese la cantidad de desaprobados "))
        cant_alumnos = cant_aprobados + cant_desaprobados
        promedio_aprobados = cant_aprobados*100/cant_alumnos
        promedio_desaprobados = cant_desaprobados*100/cant_alumnos
    print(f"El promedio de alumnos desaprobados fue del {promedio_desaprobados}% y el promedio de alumnos aprobados fue del {promedio_aprobados}% ")
elif (dia_letra == "lunes" or dia_letra == "martes" or dia_letra=="miercoles") and (dia_numero>=10 and dia_numero<=31) and (mes_actual>=10 and mes_actual<=12):
    print(f"Fecha actual: {dia_letra} , {dia_numero} / {mes_actual}") 
    examen_validar=input("¿Se tomaron exámenes? si/no ")
    examen_validar= examen_validar.lower()
    if examen_validar == "si":
        cant_aprobados = int(input("Ingrese la cantidad de aprobados "))
        cant_desaprobados = int(input("Ingrese la cantidad de desaprobados "))
        cant_alumnos = cant_aprobados + cant_desaprobados
        promedio_aprobados = cant_aprobados*100/cant_alumnos
        promedio_desaprobados = cant_desaprobados*100/cant_alumnos
        print(f"El promedio de alumnos desaprobados fue del {promedio_desaprobados}% y el promedio de alumnos aprobados fue del {promedio_aprobados}% ")
elif dia_letra == "jueves":
    print(f"Fecha actual: {dia_letra} , {dia_numero} / {mes_actual}") 
    asistencia = float(input("Ingrese el procentajes de asistencia "))
    if(asistencia > 50):
        print("Asistio a la mayoría de clases")
    else:
        print("No asistió a la mayoría de clases")
elif (dia_letra == "jueves") and (dia_numero>=1 and dia_numero<=9):
    print(f"Fecha actual: {dia_letra} , 0{dia_numero} / {mes_actual}") 
    asistencia = float(input("Ingrese el procentajes de asistencia "))
    if(asistencia > 50):
        print("Asistio a la mayoría de clases")
    else:
        print("No asistió a la mayoría de clases")
elif (dia_letra == "jueves") and (mes_actual>=1 and mes_actual<=9):
    print(f"Fecha actual: {dia_letra} , {dia_numero} / 0{mes_actual}") 
    asistencia = float(input("Ingrese el procentajes de asistencia "))
    if(asistencia > 50):
        print("Asistio a la mayoría de clases")
    else:
        print("No asistió a la mayoría de clases")
elif (dia_letra == "jueves") and (dia_numero>=10 and dia_numero<=31) and (mes_actual>=10 and mes_actual<=12):
    print(f"Fecha actual: {dia_letra} , 0{dia_numero} / {mes_actual}") 
    asistencia = float(input("Ingrese el procentajes de asistencia "))
    if(asistencia > 50):
        print("Asistio a la mayoría de clases")
    else:
        print("No asistió a la mayoría de clases")

if (dia_numero == 1 and  mes_actual == 1) or (dia_numero == 1 and mes_actual==7) and dia_numero>=1 and dia_numero<=9:
    print("Comienzo de nuevo ciclo")
    print(f"Fecha actual: {dia_letra} , 0{dia_numero} / 0{mes_actual}")
    cant_alumnosCiclo= int(input("Ingrese la cantidad de alumnos del ciclo "))
    arancel = float(input("Ingrese el arancel por alumno "))
    recaudacion = arancel * cant_alumnosCiclo
    print(f"La recaudación fue de {recaudacion}")