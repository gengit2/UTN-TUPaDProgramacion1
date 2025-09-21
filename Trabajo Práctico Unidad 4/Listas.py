#Ejercicio 1
for i in range(1,101):
    if i % 4 == 0: 
        print(i)

#Ejercicio 2 
frutas=["manzana", "banana", "pera", "damasco", "frutilla"]
print(frutas[-2])

#Ejercicio 3
lista=[]
lista.append("manzana")
lista.append("banana")
lista.append("pera")
print(lista)

#Ejercicio 4 

animales = ["perro", "gato", "conejo", "pez"]

animales[1]="loro"
animales[-1]="oso"

print(animales)

#EJercicio 5 
numeros=[8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)

#La funcion max devuelve el número máximo del arreglo es decir 22, y remove(22) elimina el numero 22 del arreglo mostrando "[8, 15, 3, 7]" 

#Ejercicio 6 
numeros=[]
for i in range(10, 31, 5):  
    numeros.append(i)

print(numeros[0], numeros[1])

#Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3]=["BMW",1]

#Ejercicio 8
numeros=[5,10,15]
dobles=[]

for i in numeros:
    dobles.append(i*2)

print(dobles)

#Ejercicio 9 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")
ind=compras[1].index("fideos")
compras[1][ind]="tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10 

lista_anidada= [[15],[True],[25.5, 57.9, 30.6],[False]]
print(lista_anidada)