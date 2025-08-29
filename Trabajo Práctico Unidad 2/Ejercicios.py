#Ejercicio 1
edad=int(input("Indique su edad "))

if edad > 18:
    print("Es mayor de edad")

#Ejercicio 2
nota=int(input("Indique su nota "))

if nota>=6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3 
num=int(input("Ingrese un número par "))

if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par ")

#Ejercicio 4 
edad= int(input("Ingrese su edad "))

if edad < 12:
    print("Niño/a")
elif edad >=12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto")

#Ejercicio 5

clave=input("Ingrese su contraseña ")

if len(clave) >=8 and len(clave) <=14:
    print("Ha ingresado una contraseña de longitud adecuada")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 12 caracteres")

#Ejercicio 6

import random
numeros_aleatorios=[random.randint(1,100) for i in range(50)]

import statistics
media = statistics.mean(numeros_aleatorios)

mediana= statistics.median(numeros_aleatorios)

moda = statistics.mode(numeros_aleatorios)

if (media > mediana) and (mediana > moda):
    print("Sesgo positivo o a la derecha")
elif(media < mediana) and (mediana < moda):
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")

#Ejercicio 7
frase = input("Ingrese una frase ").lower()
ult_letra=frase[-1]

if ult_letra in ("aeiou"):
    print(frase,"!")
else:
    print(frase)

#Ejercicio 8
nombre=input("Ingrese su nombre: ")
opcion = input("Ingrese una opción (1).Si quiere su nombre en mayúsculas (2).Si quiere su nombre en minúsculas (3).Si quiere solo su nombre con la primera letra en mayúsculas ")

if opcion == "1":
    nombre= nombre.upper()
    print(nombre)
elif opcion == "2":
    nombre= nombre.lower()
    print(nombre)
elif opcion == "3":
    nombre=nombre.title()
    print(nombre)

#Ejercicio 9
escala_terr=int(input("Ingrese la magnitud del terremoto en la escala Richter "))

if escala_terr <3 and escala_terr > 0:
    print("Muy leve")
elif escala_terr >= 3 and escala_terr < 4:
    print("Leve")
elif escala_terr >= 4 and escala_terr < 5:
    print("Moderado")
elif escala_terr >= 5 and escala_terr < 6:
    print("Fuerte")
elif escala_terr >= 6 and escala_terr < 7:
    print("Muy Fuerte")
elif escala_terr >= 7:
    print("Extremo")

#Ejercicio 10 
hemisferio= input("¿En hemisferio se encuentra Norte o Sur [N/S]? ").lower()
mes=input("¿En qué mes se encuentra? ").lower()
dia=int(input("¿En qué dia del mes se encuentra? (en números) "))

inv_nort=["diciembre","enero", "febrero","marzo"]
prim_nort=["marzo", "abril", "mayo", "junio"]
veran_nort=["junio", "julio", "agosto", "septiembre"]
oto_nort=["septiembre", "octubre", "noviembre", "diciembre"]

veran_sur=["diciembre","enero", "febrero","marzo"]
oto_sur=["marzo", "abril", "mayo", "junio"]
inv_sur=["junio", "julio", "agosto", "septiembre"]
prim_sur=["septiembre", "octubre", "noviembre", "diciembre"]

if hemisferio=="n":
    if (((mes in inv_nort) and (dia>=21)) or ((mes in inv_nort) and (dia<=20))) and dia<=31:  
        print("Invierno")
    elif (((mes in prim_nort) and (dia>=21)) or ((mes in prim_nort) and (dia<=20))) and dia<=31:
        print("Primavera")
    elif (((mes in oto_nort) and (dia>=21)) or ((mes in oto_nort) and (dia<=20))) and dia<=31:
        print("Otoño")
    elif (((mes in veran_nort) and (dia>=21)) or ((mes in veran_nort) and (dia<=20))) and dia<=31:
        print("Verano")
    else:
        print("Algún dato es inválido")
elif hemisferio=="s":
    if (((mes in inv_sur) and (dia>=21)) or ((mes in inv_sur) and (dia<=20))) and dia<=31:
        print("Invierno")
    elif (((mes in prim_sur) and (dia>=21)) or ((mes in prim_sur) and (dia<=20))) and dia<=31:
        print("Primavera")
    elif (((mes in oto_sur) and (dia>=21)) or ((mes in oto_sur) and (dia<=20))) and dia<=31:
        print("Otoño")
    elif (((mes in veran_sur) and (dia>=21)) or ((mes in veran_sur) and (dia<=20))) and dia<=31:
        print("Verano")
    else:
        print("Algún dato es inválido")
else:
    print("Hemisferio inválido")     