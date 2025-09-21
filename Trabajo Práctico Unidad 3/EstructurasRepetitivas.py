#Ejercicio 1

for nro in range(0,101):
    print(nro)

#Ejercicio 2 

nro=int(input("Ingrese un número entero "))
digitos=0
numCopia=nro

while nro>0:
    digitos+=1
    nro//=10

if numCopia==0:
    print("Colocó el número 0 ")
else:
    print(f"La cantidad de dígitos es: {digitos}")

#Ejercicio 3 

inicio=int(input("Ingrese un número de inicio entero "))
final= int(input("Ingrese un número final entero "))
sumatoria=0

for nro in range(inicio+1,final):
    sumatoria+=nro    

print(f"La suma de los números enteros desde {inicio} hasta {final} sin contar {final} ni {inicio} es: {sumatoria}")

#Ejercicio 4

nro=int(input("Ingrese números enteros para sumar. Ingrese 0 para mostrar la suma "))
suma=0
numCopia=nro
while nro!=0:
    suma+=nro
    nro=int(input("Ingrese otro número "))

if numCopia==0:
    print("Colocó el número 0")
else:
    print(f"La sumatoria es {suma}")

#Ejercicio 5

import random
numAleatorio=random.randint(0,9)
intentos=0
nro=int(input("Adivina el número aleatorio entre 0 y 9"))

while nro != numAleatorio:
    intentos+=1
    nro=int(input("Intenta con otro número"))

if intentos == 0:
    print(f"El número era {numAleatorio}. A la primera! Intentos: {intentos+1}")
else:
    print(f"El número era {numAleatorio}. Intentos: {intentos}")

#Ejercicio 6 

for num in range(100,0,-1):
    if num%2==0:
        print(num)

#Ejercicio 7

nro=int(input("Ingrese un número entero límite para sumas los números desde el 0 "))
suma=0

for num in range(0,nro+1):
    suma+=num

if nro<0:
    print("Ingrese un número positivo")
else:
    print(f"La suma desde 0 hasta {nro} es: {suma}")

#Ejercicio 8 

cantEnteros=10
contPositivos=0
contNegativos=0
contPares=0
contImpares=0

for num in range(cantEnteros):
    nro=int(input(f"Ingrese número {num+1} "))
    if nro>0:
        contPositivos+=1
    elif nro == 0:
        print("0 Número nulo")
    else:
        contNegativos+=1

    if nro%2==0:
        contPares+=1
    else:
        contImpares+=1

print(f"Cantidad positivos: {contPositivos}, cantidad negativos: {contNegativos}, cantidad pares: {contPares}, cantidad impares: {contImpares}")

#Ejercicio 9

cantEnteros=10
suma=0
promedio=0
print(f"Ingrese {cantEnteros} enteros")

for num in range(cantEnteros):
    nro=int(input(f"Ingrese entero nro: {num+1}" + " "))
    suma+=nro

promedio=suma/cantEnteros
print(f"El promedio de los números sumados es de: {promedio}")

#Ejercicio 10 

num = int(input("Ingrese un número para invertirlo "))
digito=0
invertido=0
numCopia= num
while num > 0:
    digito=num%10
    invertido=invertido*10+digito
    num//=10

if numCopia<=0:
    print("Ingrese número positivo mayor a 0")
else:
    print(f"El número invertido es {invertido}")