from funciones import disparar, iniciar_juego

tablero = iniciar_juego()

vidas = 10

while vidas > 0:
    tablero = disparar(tablero)
    print(tablero)


