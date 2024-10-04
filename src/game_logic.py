import random

def seleccionar_palabra():
    with open("words.txt", "r") as file:
        palabras = file.readlines()
    print("La palabra ha sido seleccionada. ¡Comienza a adivinar!")
    return random.choice(palabras).strip()