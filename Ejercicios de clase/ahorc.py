import random

palabras=["manzana","banana", "pera", "palta", "zanahoria", "nuez", "maiz", "frutilla"]

dib_ahorc=[
    """
    +---+
    |   |
        |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    """,
    """
    +---+
    |    |
    O    |
    /|   |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    /|\ |
        |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    /|\ |
    /   |
        |
    =========
    """,
    """
    +---+
    |   |
    O   |
    /|\ |
    / \ |
        |
    =========
    """
]

def eleccion_palabra():
    #Elige una palabra 
    return random.choice(palabras)

def tablero_ver(palabra, letras_adivinadas):
    
    tablero = ""  
    for letra in palabra:
        if letra in letras_adivinadas:
            tablero += letra + " "  
        else:
            tablero += "_ "  
    print(tablero.strip())  

def pedir_letra(letras_usadas):
    while True:
        letra= input("Ingrese una letra: ").lower()

        if len(letra)!= 1 or not letra.isalpha():
            print("Ingrese una letra válida")
            continue

        elif letra in letras_usadas: 
            print("Ya usaste esa letra")
            continue

        else:
            return letra
        
def ver_letras_usadas(letras_usadas):
    texto=""

    for l in letras_usadas:
        texto+=l + ""
    
    print(texto)

def jugar():
    palabra=eleccion_palabra()
    letras_correctas= []
    letras_usadas= []
    intentos_restantes=6

    print("Bienvenido")

    while intentos_restantes>0:
        print(dib_ahorc[6-intentos_restantes])
        tablero_ver(palabra, letras_correctas)
        ver_letras_usadas(letras_usadas)
        print("Intentos restantes: ", intentos_restantes)

        letra=pedir_letra(letras_usadas)
        letras_usadas.append(letra)

        if letra in palabra:
            letras_correctas.append(letra)
            print("Letra adivinada")
        else:
            intentos_restantes-=1
            print("Letra incorrecta")
        
        gano= True
        for l in palabra:
            if l not in letras_correctas:
                gano=False
                break
        
        if gano:
            print(f"Has ganado, palabra = {palabra}")
            return
    
    print(dib_ahorc[-1])
    print(f"Palabra no adivinada, palabra = {palabra}")

jugar()








