import numpy as np

def crear_tablero(tamaño=(10,10)):
    return np.full(tamaño, "_")


def generar_barco(eslora):
    if eslora == 2:
        return [(1,1),(1,2)]
    else:
        return [(4,5),(5,5), (6,5)]
    

def colocar_barco(tablero, barco):
    for casilla in barco:
        tablero[casilla] = "O"
    return tablero


def disparar(tablero):
    fila = int(input("Introduzca la fila donde disparar"))
    columna = int(input("Introduzca la columna donde disparar"))
    casilla = (fila, columna)
    if tablero[casilla] == "_":
        print("Agua, has fallado")
        tablero[casilla] = "A"
    else:
        print("Tocado, has acertado")
        tablero[casilla] = "X"
    return tablero

def iniciar_juego():
    tablero = crear_tablero()

    barco_1 = generar_barco(2)
    tablero = colocar_barco(tablero, barco_1)

    barco_2 = generar_barco(4)
    tablero = colocar_barco(tablero, barco_2)
    return tablero