import random

def seleccionar_palabra():
    with open("words.txt", "r") as file:
        palabras = file.readlines()
    print("La palabra ha sido seleccionada. ¡Comienza a adivinar!")
    return random.choice(palabras).strip()

def adivinar_letra(letra, palabra, progreso,intentos_restantes):
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                progreso[i] = letra
        return True, intentos_restantes
    else:
        return False, intentos_restantes - 1