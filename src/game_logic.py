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

def dar_pista(palabra, progreso, cont_pistas):
    while True:
        pista = random.choice(palabra)
        if pista not in progreso:
            for i in range(len(palabra)):
                if palabra[i] == pista:
                    progreso[i] = pista
            break
    cont_pistas -= 1
    print(f"La pista es la letra {pista}. Te quedan {cont_pistas} pistas.")
    return progreso, cont_pistas
