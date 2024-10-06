from src.game_logic import seleccionar_palabra, adivinar_letra, dar_pista, verificar_fin_juego


def main():
    print("Bienvenido al Juego de Adivinanza de Palabras!")
    palabra_secreta = seleccionar_palabra()
    progreso = ["_"] * len(palabra_secreta)
    intentos_restantes = 5
    pistas_restantes = 2

    while True:
        print("Palabra: ", " ".join(progreso))

        # Pista
        if pistas_restantes > 0 and input("¿Quieres una pista? (s/n): ").lower() == "s":
            progreso, pistas_restantes = dar_pista(palabra_secreta, progreso, pistas_restantes)
            continue

        # Adivinar letra
        letra = input("Adivina una letra: ")
        adivina, intentos_restantes = adivinar_letra(letra, palabra_secreta, progreso, intentos_restantes)
        if adivina:
            print(f"¡Correcto! La letra {letra} está en la palabra.")
        else:
            print(f"¡Incorrecto! La letra {letra} no está en la palabra. Te quedan {intentos_restantes} intentos.")

        # Verificar si el juego ha terminado
        resultado = verificar_fin_juego(progreso, intentos_restantes)
        if resultado == "victoria":
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
            break
        elif resultado == "derrota":
            print(f"¡Perdiste! La palabra era: {palabra_secreta}")
            break

if __name__ == "__main__":
    main()
