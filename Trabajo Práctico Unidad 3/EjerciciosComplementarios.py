#Ejercicio 1

for i in range(2,21,2):
    if i%2==0:
        print(i)

#Ejercicio 2 

num=int(input("Ingrese numeros enteros, cuando la suma supero 100 se mostrará por pantalla "))
suma=num
while suma<100:
    num=int(input("Ingrese numeros enteros, cuando la suma supere 100 se mostrará por pantalla "))
    suma+=num

print(f"Suma: {suma}")

#Ejercicio 3
palabras=["apple", "banana", "avocado"]
for i in palabras:
    if i[0]=='a':
        print(i)

#Ejercicio 4

num=int(input("Ingrese un número para saber su tabla de multiplicar "))

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

#Ejercicio 5 

frase = input("Ingrese una fase para contar vocales ")
vocales="aeiouAEIOU"
contador=0
for letra in frase:
    if letra in vocales:
        contador+=1

print(f"Vocales: {contador}")

#Ejercicio 6 

lista1=[3,1,3,1,5]
lista2=[]

for elemento in lista1:
    if lista1.count(elemento)>1 and elemento not in lista2:
        lista2.append(elemento)

print(lista2)

#Ejercicio 7

for i in range(1,101):
    print(i)
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
        if i%5==0 and i%3==0:
            print("FizzBuzz")

#