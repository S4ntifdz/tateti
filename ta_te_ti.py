import os
l = [[0, 0, 0], 
     [0, 0, 0],
     [0, 0, 0]]
#--------------------------------------------
def validaciones(l):
    for i in range(3):
        if l[i][0] == l[i][1] == l[i][2] != 0:
            return l[i][0]
        if l[0][i] == l[1][i] == l[2][i] != 0:
            return l[0][i]
    if l[0][0] == l[1][1] == l[2][2] != 0:
        return l[0][0]
    if l[0][2] == l[1][1] == l[2][0] != 0:
        return l[0][2]
    return 0
#--------------------------------------------
def turnos(x):
    if x == True:
        jugador = 1
        print ("Jugador 1:")
        fila = int(input("Ingrese fila (F): "))
        columna = int(input("Ingrese columna (C): "))
        x = False
    else:
        jugador = 2
        print ("Jugador 2:")
        fila = int(input("Ingrese fila (F): "))
        columna = int(input("Ingrese columna (C): "))
        x = True
    return fila, columna, x, jugador
#--------------------------------------------
def tablero(l):
    print("F\C 0   1   2") 
    for i in range(3):
        for j in range(3):
            if j == 0:
                print(i,"|", end=" ")
            print( l[i][j], end= " | ") 
        print()


#--------------------------------------------   
def main():
    band = True
    juego = True
    lleno = 0
    while juego:
        os.system('cls')
        tablero(l)
        #print (band)
        fila, columna, band, jugada = turnos(band)
        if l[fila][columna] == 0:
            l[fila][columna] = jugada
            lleno += 1
        else:
            repite = True
            while (repite):
                print("La casilla ya esta ocupada")
                band = not band
                fila, columna, band, jugada = turnos(band)
                if l[fila][columna] == 0:
                    l[fila][columna] = jugada
                    lleno += 1
                    repite = False

        fin = validaciones(l)

        if fin == 1:
            juego = False
            tablero(l)
            print("Ganador: Jugador 1")
            
        elif fin == 2:
            juego = False
            tablero(l)
            print("Ganador: Jugador 2")
        elif lleno == 9:
            juego = False
            tablero(l)
            print("Empate")

    print("Fin del juego")

main()

