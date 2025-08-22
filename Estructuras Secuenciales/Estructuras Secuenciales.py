

#Ejercicio 1

print("Hola Mundo")

#Ejercicio 2 

nombre = input("Ingrese su nombre ")
print(f"Hola, {nombre}!")

#Ejercicio 3

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = int(input("Ingrese su edad "))
residencia = input("Ingrese su residencia ")
print(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {residencia}")

#Ejercicio 4

radio= float(input("Ingrese el radio del círculo "))
PI=3.14
area= PI*radio**2
perimetro= 2*PI*radio
print(f"El perímetro es de: {perimetro} cm y el área es de: {area} cm")

#Ejercicio 5 

segundos=int(input("Ingrese la cantidad de segundos para pasarlo a horas "))
hora= segundos/3600
print(f"{segundos} segundos, equivalen a {hora} horas")

#Ejercicio 6

numero = int(input("Ingrese un número para mostrar su tabla de multiplicar "))
print(f"{numero} x 1 =",numero*1)
print(f"{numero} x 2 =",numero*2)
print(f"{numero} x 3 =",numero*3)
print(f"{numero} x 4 =",numero*4)
print(f"{numero} x 5 =",numero*5)
print(f"{numero} x 6 =",numero*6)
print(f"{numero} x 7 =",numero*7)
print(f"{numero} x 8 =",numero*8)
print(f"{numero} x 9 =",numero*9)
print(f"{numero} x 10 =",numero*10)

#Ejercicio 7 

num1=int(input("Ingrese el primer número "))
num2=int(input("Ingrese el segundo número "))
print(f"{num1} + {num2}=",num1+num2)
print(f"{num1} - {num2}=",num1-num2)
print(f"{num1} * {num2}=",num1*num2)
print(f"{num1} / {num2}=",num1/num2)

#Ejercicio 8

kilogramos= float(input("Ingrese su peso en kiligramos "))
altura= float(input("Ingrese su altura en metros "))
imc= kilogramos/(altura**2)
print("Su índice de masa corporal es de ", imc)

#Ejercicio 9

grados_celsius= float(input("Ingrese su temperatura en grados celsius "))
grados_fahrenheit= 9/5*grados_celsius + 32
print(f"{grados_celsius} grados celsius equivalen a {grados_fahrenheit} grados fahrenheit")

#Ejercicio 10 

num1=float(input("Ingrese el primer número "))
num2=float(input("Ingrese el segundo número "))
num3= float(input("Ingrese el tercer número "))
suma= num1+num2+num3
promedio=suma/3
print(f"El promedio es de: {promedio}")